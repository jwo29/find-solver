import json
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


def search_solver(problem_no):

    try:
        with open('./data/solved-db.json', 'r', encoding='utf-8') as problem_file:
            members = json.load(problem_file)

            solvers = []

            for member in members:
                solved_list = member["solved"]

                if problem_no in solved_list:
                    solvers.append(member["id"])

            return solvers

    except FileNotFoundError:
        logger.debug("Failed to read Solved DB file")

        return "FileNotFoundError - Failed to read Solved DB file"