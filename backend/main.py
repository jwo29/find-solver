from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from service.boj_crawler import *
from service.search_solver import search_solver
from service.time_service import get_last_udt

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8077",
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

    result = search_solver(problem_no)

    return JSONResponse(result)


# 멤버 갱신
@app.post("/members")
def update_member():

    result = member_crawler()

    return JSONResponse(result)


# 푼 문제 갱신
@app.post("/problems")
def update_problem():

    result = problem_crawler()

    return JSONResponse(result)

# 마지막 업데이트 시간 얻기
@app.get("/lastUpdateTime")
def get_update_time():

    result = get_last_udt()

    return JSONResponse(result)
