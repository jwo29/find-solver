import json

from datetime import datetime
from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
# from fastapi.responses import HTMLResponse, FileResponse

from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from selenium import webdriver
from selenium.webdriver.common.by import By

from service.boj_crawler import *
from service.search_solver import search_solver

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

    solvers = search_solver(problem_no)

    return JSONResponse({
        'result': 1 if solvers else 0,
        'solver_num': len(solvers),
        'solvers': solvers
    })


# 멤버 갱신
@app.post("/members")
def update_member():

    last_update_time = str(datetime.now())

    result = member_crawler()

    return JSONResponse({
        'last_update_time': last_update_time
    })


# 푼 문제 갱신
@app.post("/problems")
def update_problem():

    last_update_time = str(datetime.now())

    result = problem_crawler()

    return JSONResponse({
        'last_update_time': last_update_time
    })
