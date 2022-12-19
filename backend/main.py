import json

from datetime import datetime
from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
# from fastapi.responses import HTMLResponse, FileResponse

from fastapi.responses import FileResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware

from selenium import webdriver
from selenium.webdriver.common.by import By

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    # "https://gist.githubusercontent.com/jwo29/f19f815b9bdf216c9590d6678c067b0d/raw/3f9229d7c26484d5b3c676241c3f5b9e1d1c28f6/test.json"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 백준 scv 그룹 랭킹 url
# https://www.acmicpc.net/group/ranklist/9848
GROUP_ID = 9848


@app.get("/")
async def home():
    return "hello"


@app.get("/problems/{problem_no}")
async def get_solver(problem_no: str):
    # do something

    with open('./data/solved-db.json', 'r', encoding='utf-8') as problem_file:
        members = json.load(problem_file)

        solvers = []

        for member in members:
            solved_list = member["solved"]

            if problem_no in solved_list:
                solvers.append(member["id"])

        return JSONResponse({
            'result': 1 if solvers else 0,
            'solver_num': len(solvers),
            'solvers': solvers
        })


# 멤버 갱신
@app.post("/members")
async def update_member():

    last_update_time = datetime.now()

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # apt install chromium-chromedriver
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.acmicpc.net/group/ranklist/{}".format(GROUP_ID))

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

    return JSONResponse({
        'last_update_time': last_update_time
    })


# 푼 문제 갱신
@app.post("/problems")
async def update_problem():

    last_update_time = datetime.now()

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # apt install chromium-chromedriver
    solved_list = []

    with open('./data/member-db.json', 'r', encoding='utf-8') as f:
        members = json.load(f)

        # print(members)
        for member in members:
            member_id = member['id']

            driver = webdriver.Chrome(options=options)
            driver.get("https://www.acmicpc.net/user/{}".format(member_id))

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
        # end of for
    # close file

    # solved-db.json으로 저장
    with open('./data/solved-db.json', 'w', encoding='utf-8') as outfile:
        json.dump(solved_list, outfile, ensure_ascii=False)

    return JSONResponse({
        'last_update_time': last_update_time
    })
