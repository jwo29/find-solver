import json

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


@app.get("/")
async def home():
    return "hello"


@app.get("/solver")
async def test():
    # return FileResponse('./backend/data/solved-db.json', media_type="application/json")
    # return FileResponse('./backend/data/test.json', media_type="application/json")
    return JSONResponse([
        {
            "id": "user1",
            "solved": ["1000", "1001", "2000", "2001"]
        },
        {
            "id": "user2",
            "solved": ["2000", "2002"]
        },
        {
            "id": "user3",
            "solved": ["1000", "2001", "2002"]
        }
    ])

# 멤버 갱신
@app.post("/member")
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
    with open('./backend/data/member-db.json', 'w', encoding='utf-8') as outfile:
        json.dump(members, outfile, ensure_ascii=False)
    

# 푼 문제 갱신
@app.post("/problem")
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
            problems = list(map(str, problems))

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
    with open('./backend/data/solved-db.json', 'w', encoding='utf-8') as outfile:
        json.dump(solveds, outfile, ensure_ascii=False)    

    return 'success'

@app.post("/test")
async def test():
    print('test!!!!!')
    return JSONResponse([
        {
            "id": "user1",
            "solved": ["1000", "1001", "2000"]
        },
        {
            "id": "user2",
            "solved": ["2000", "2002"]
        }
    ])