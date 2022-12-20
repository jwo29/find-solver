import json
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


def search_solver(problem_no):

    result_obj = {}
    result_msg = ""

    try:
        with open('./data/solved-db.json', 'r', encoding='utf-8') as problem_file:
            solved_db = json.load(problem_file)

            solvers = []

            for member in solved_db['solved_info']:
                solved_list = member["solved"]

                if problem_no in solved_list:
                    solvers.append(member["id"])

            result_obj['solver_num'] = len(solvers)
            result_obj['solvers'] = solvers
            result_msg = "Success"

    except FileNotFoundError:
        logger.debug("Failed to read Solved DB file")

        result_msg = "FileNotFoundError - Failed to read Solved DB file"

    finally:

        result_obj['result_msg'] = result_msg

    return result_obj
