import json
import logging
import schedule

from datetime import datetime

from selenium import webdriver
from selenium.common import SessionNotCreatedException
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

# 백준 SCV 그룹 랭킹 URL
# https://www.acmicpc.net/group/ranklist/9848
GROUP_ID = 9848

date_format = "%Y.%m.%d %H:%M:%S"

def member_crawler():
    result_obj = {}
    result_msg = ""

    # 멤버 정보를 json 포맷으로 저장
    member_db = {}
    members = []  # member_db['members'] = members

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # apt install chromium-chromedriver
    try:
        
        # 마지막 업데이트 시간 갱신
        member_db['last_update_time'] = datetime.now().strftime(date_format)

        driver = webdriver.Chrome(options=options)
        driver.get("https://www.acmicpc.net/group/ranklist/{}".format(GROUP_ID))

        try:
            # 멤버 리스트 가져오기
            member_list = driver.find_elements(By.CSS_SELECTOR, '#ranklist > tbody > tr')

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

            member_db['members'] = members

            # dump 저장 시 한글 깨짐 현상 해결: ensure_ascii=False
            with open('./data/member-db.json', 'w', encoding='utf-8') as outfile:
                json.dump(member_db, outfile, ensure_ascii=False)

            result_msg = "Success"
            result_obj['last_update_time'] = member_db['last_update_time']

        except NoSuchElementException:
            logger.debug("Can not parse the DOM element")

            result_msg = "NoSuchElementException - Can not parse the DOM element"

    except SessionNotCreatedException:
        logger.debug("Current Chrome Driver's version is lower than using Chrome Browser's version")

        result_msg = "SessionNotCreatedException - Current Chrome Driver's version is lower than using Chrome Browser's version"
    finally:

        result_obj['result_msg'] = result_msg

    return result_obj


def problem_crawler():
    result_obj = {}
    result_msg = ""

    # 문제 정보를 json 포맷으로 저장
    solved_db = {}
    solved_info = []  # solved_db['solved_info'] = solved_info

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # apt install chromium-chromedriver

    try:
        with open('./data/member-db.json', 'r', encoding='utf-8') as f:
            member_db = json.load(f)

            # print(members)
            for member in member_db['members']:
                member_id = member['id']

                try:

                    # 마지막 업데이트 시간 갱신
                    solved_db['last_update_time'] = datetime.now().strftime(date_format)

                    driver = webdriver.Chrome(options=options)
                    driver.get("https://www.acmicpc.net/user/{}".format(member_id))

                    try:
                        element = driver.find_element(By.CLASS_NAME, 'problem-list')

                        problems = element.text
                        problems = problems.split(' ')
                        problems = list(map(str, problems))

                        # print(problems)

                        solved_info.append(
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

            solved_db['solved_info'] = solved_info

        # close file

        # solved-db.json으로 저장
        with open('./data/solved-db.json', 'w', encoding='utf-8') as outfile:
            json.dump(solved_db, outfile, ensure_ascii=False)

        result_msg = "Success"
        result_obj['last_update_time'] = solved_db['last_update_time']

    except FileNotFoundError:
        logger.debug("Failed to read Member DB file")

        result_msg = "FileNotFoundError - Failed to read Member DB file"

    finally:

        result_obj['result_msg'] = result_msg

    return result_obj


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
