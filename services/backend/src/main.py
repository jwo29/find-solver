from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.service.bojCrawler import *
from src.service.findSolver import find_solvers
from src.service.timeService import get_last_udt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"], # Vue.js address. AWS instance의 public ip/port로 변경할 것
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "hello"


# 푼 멤버 검색
@app.get("/members/{problem_no}")
def get_solver(problem_no: str):

    result = find_solvers(problem_no)

    return JSONResponse(result)


## 멤버 갱신
@app.post("/members")
async def update_member():

    result = member_crawler()

    return JSONResponse(result)


## 푼 문제 갱신
@app.post("/problems")
async def update_problem():

    result = problem_crawler()

    return JSONResponse(result)


## 마지막 업데이트 시간 얻기
@app.get("/lastUpdateTime")
def get_update_time():

    result = get_last_udt()

    return JSONResponse(result)
