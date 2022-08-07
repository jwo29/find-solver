from msilib.schema import File
from fastapi import FastAPI
# from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
# from starlette.responses import JSONResponse

from selenium import webdriver
from selenium.webdriver.common.by import By


app = FastAPI()


fask_db = {
    
}


class User(BaseModel):
    uid: str
    solved: list

# @app.get("/", response_class=HTMLResponse)
# async def home():
#     return """
#     <form action="/test" method="get">
#         <button type="submit" formmethod="GET">전체 멤버의 푼 문제 불러오기</button>
#     </form>
#     """

@app.get("/", response_class=FileResponse)
async def home():
    return './backend/index.html'

@app.get("/test")
async def home():
    from selenium import webdriver
    from selenium.webdriver.common.by import By


    def get_solved_problem(name='january'):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        # apt install chromium-chromedriver

        with open('db.txt', 'r') as f:
            for uname in f:
                print(f'uname: {uname}')

                driver = webdriver.Chrome(options=options)
                driver.get("https://www.acmicpc.net/user/{}".format(uname))
                element = driver.find_element(By.CLASS_NAME, 'problem-list')

                problems = element.text
                problems = problems.split(' ')
                problems = list(map(int, problems))

                print(problems)

                # uname, solved를 속성으로 가지는 json 목록 만들어서 solved_db.txt에 저장
                # 안정화 및 최적화되면 db.txt -> memeber_db.txt로 변경 후
                # member_db.txt에 scv 멤버 저장하기      
                # 
                # 백준 scv 그룹 랭킹 url
                # https://www.acmicpc.net/group/ranklist/9848      


    # print('problems:', get_solved_problem())
    get_solved_problem()

    return 'success'
