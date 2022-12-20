import json
import logging
import schedule

from selenium import webdriver
from selenium.common import SessionNotCreatedException
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

# 백준 SCV 그룹 랭킹 URL
# https://www.acmicpc.net/group/ranklist/9848
GROUP_ID = 9848


def member_crawler():

    result_msg = ""

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # apt install chromium-chromedriver
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.acmicpc.net/group/ranklist/{}".format(GROUP_ID))

        try:
            # 멤버 리스트 가져오기
            member_list = driver.find_elements(By.CSS_SELECTOR, '#ranklist > tbody > tr')

            # 각 멤버의 정보를 json객체로 저장
            members = []

            for member in member_list:
                info = member.find_elements(By.TAG_NAME, 'td')

                members.append(
                    {
                        'rank': int(info[0].text),  # 등수
                        'id': info[1].text,  # 아이디
                        'message': info[2].text,  # 상태 메시지
                        'num-of-solving': int(info[3].text),  # 맞은 문제
                        'num-of-submit': int(info[4].text),  # 제출
                        'pct-cor-ans': info[5].text  # 정답 비율
                    }
                )

            # dump 저장 시 한글 깨짐 현상 해결: ensure_ascii=False
            with open('./data/member-db.json', 'w', encoding='utf-8') as outfile:
                json.dump(members, outfile, ensure_ascii=False)

            result_msg = "1"

        except NoSuchElementException:
            logger.debug("Can not parse the DOM element")

            result_msg = "NoSuchElementException - Can not parse the DOM element"

    except SessionNotCreatedException:
        logger.debug("Current Chrome Driver's version is lower than using Chrome Browser's version")

        result_msg = "SessionNotCreatedException - Current Chrome Driver's version is lower than using Chrome Browser's version"

    return result_msg


def problem_crawler():

    result_msg = ""

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # apt install chromium-chromedriver
    solved_list = []

    try:
        with open('./data/member-db.json', 'r', encoding='utf-8') as f:
            members = json.load(f)

            # print(members)
            for member in members:
                member_id = member['id']

                try:
                    driver = webdriver.Chrome(options=options)
                    driver.get("https://www.acmicpc.net/user/{}".format(member_id))

                    try:
                        element = driver.find_element(By.CLASS_NAME, 'problem-list')

                        problems = element.text
                        problems = problems.split(' ')
                        problems = list(map(str, problems))

                        # print(problems)

                        solved_list.append(
                            {
                                'id': member_id,
                                'solved': problems
                            }
                        )

                    except NoSuchElementException:
                        logger.debug("Can not parse the DOM element")

                        result_msg = "NoSuchElementException - Can not parse the DOM element"

                except SessionNotCreatedException:
                    logger.debug("Current Chrome Driver's version is lower than using Chrome Browser's version")

                    result_msg = "SessionNotCreatedException - Current Chrome Driver's version is lower than using Chrome Browser's version"
            # end of for
        # close file

        # solved-db.json으로 저장
        with open('./data/solved-db.json', 'w', encoding='utf-8') as outfile:
            json.dump(solved_list, outfile, ensure_ascii=False)

        result_msg = "1"

    except FileNotFoundError:
        logger.debug("Failed to read Member DB file")

        result_msg = "FileNotFoundError - Failed to read Member DB file"

    return result_msg


## 1. 크롤링 스케줄 등록

# 1-1. 멤버 업데이트 -> 매일 오전 4시
schedule.every().day.at("04:00").do(member_crawler)

# 1-2. 문제 업데이트 -> 네시간 간격
schedule.every(4).hours.do(problem_crawler)

# ## 2. 스케줄 시작
# while True:
#
#     schedule.run_pending()
#     time.sleep(1)
