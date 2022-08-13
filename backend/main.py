import json

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
# from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel

from selenium import webdriver
from selenium.webdriver.common.by import By


app = FastAPI()


class User(BaseModel):
    uid: str
    solved: list


origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/member")
async def updateMemeber():

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # 백준 scv 그룹 랭킹 url
    # https://www.acmicpc.net/group/ranklist/9848
    GROUP_ID = 9848
    
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    
    # apt install chromium-chromedriver
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.acmicpc.net/group/ranklist/{}".format(GROUP_ID))

    # 멤버 리스트 가져오기
    memberList = driver.find_elements(By.CSS_SELECTOR, '#ranklist > tbody > tr')
    
    # 각 멤버의 정보를 json객체로 저장
    members = []
    
    for member in memberList:
        info = member.find_elements(By.TAG_NAME, 'td')
    
        members.append(
            {
                'rank': info[0].text,            # 등수
                'id': info[1].text,              # 아이디
                'message': info[2].text,         # 상태 메시지
                'num-of-solving': info[3].text,  # 맞은 문제
                'num-of-submit': info[4].text,   # 제출
                'pct-cor-ans': info[5].text      # 정답 비율
            }
        )
        
    # dump 저장 시 한글 깨짐 현상 해결: ensure_ascii=False
    with open('./member-db.json', 'w', encoding='utf-8') as outfile:
        json.dump(members, outfile, ensure_ascii=False)
    


@app.get("/problem")
async def updateProblem():

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # apt install chromium-chromedriver
    solveds = []

    with open('member-db.json', 'r', encoding='utf-8') as f:
        members = json.load(f)

        # print(members)
        for member in members:
            id = member['id']

            driver = webdriver.Chrome(options=options)
            driver.get("https://www.acmicpc.net/user/{}".format(id))
            element = driver.find_element(By.CLASS_NAME, 'problem-list')

            problems = element.text
            problems = problems.split(' ')
            problems = list(map(int, problems))

            # print(problems)

            solveds.append(
                {
                    'id': id,
                    'solved': problems
                }
            )
        # end of for
    # close file
    
    # solved-db.json으로 저장
    with open('./solved-db.json', 'w', encoding='utf-8') as outfile:
        json.dump(solveds, outfile)    

    return 'success'
