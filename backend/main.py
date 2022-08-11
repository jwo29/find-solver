import json

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from selenium import webdriver
from selenium.webdriver.common.by import By


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    uid: str
    solved: list

@app.get("/")
def read_root():
    response = {
        'data': [
            {
                'id': 1,
                'name': 'Chocolate',
                'price': '4.50',
            },
            {
                'id': 2,
                'name': 'Sorvete',
                'price': '2.42',
            },
            {
                'id': 3,
                'name': 'Refrigerante',
                'price': '4.90',
            },
            {
                'id': 4,
                'name': 'X-salada',
                'price': '7.99',
            },
        ]
    }
    return response



# @app.get("/", response_class=FileResponse)
# async def home():
    # return './backend/index.html'


# 멤버 갱신(크롤링, 미완)
@app.put("/member")
async def home():
    # from selenium import webdriver
    # from selenium.webdriver.common.by import By

    # 백준 scv 그룹 랭킹 url
    # https://www.acmicpc.net/group/ranklist/9848
    GROUP_ID = 9848

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # apt install chromium-chromedriver
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.acmicpc.net/group/ranklist/{}".format(GROUP_ID))

    element = driver.find_element(By.CSS_SELECTOR, '#ranklist > tbody > tr')
    
    # 행 길이 가져오기

    # member-id-db.txt에 업데이트
    



# 푼 문제 갱신(크롤링)
@app.put("/problem")
async def home():
    # from selenium import webdriver
    # from selenium.webdriver.common.by import By

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # apt install chromium-chromedriver
    users = {}

    with open('member-id-db.txt', 'r') as f:
        for line in f:
            uname = line.strip()
            print(f'uname: {uname.strip()}')

            driver = webdriver.Chrome(options=options)
            driver.get("https://www.acmicpc.net/user/{}".format(uname))
            element = driver.find_element(By.CLASS_NAME, 'problem-list')

            problems = element.text
            problems = problems.split(' ')
            problems = list(map(int, problems))

            print(problems)

            users[uname] = {
                'id': uname,
                'solved': problems
            }

            
            # uname, solved를 속성으로 가지는 json 목록 만들어서 solved_db.json에 저장
            # 안정화 및 최적화되면 db.txt -> memeber_db.txt로 변경 후
            # member_db.txt에 scv 멤버 저장하기      
            # 
            
        # end of for
    # end of open() 
     
    
    # users 딕셔너리를 solved_db.json으로 저장
    with open('solved-db.json', 'w') as of:
        json.dump(users, of)    
        

    return 'success'

@app.get("/test", response_class=JSONResponse)
async def test():
    with open('./solved-db.json', 'r') as f:
        data  = json.load(f)

        # for v in data.values():
            # print(f"id: {v['id']}, solved: {v['solved']}")

        return data