import json
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


def get_last_udt():
    result_obj = {}
    result_msg = ""

    # 멤버 DB 마지막 업데이트 시간
    try:
        with open('./data/member-db.json', 'r', encoding='utf-8') as f:
            member_db = json.load(f)
            result_obj['member_last_udt'] = member_db['last_update_time']
    except FileNotFoundError:
        logger.debug("Failed to read Member DB file")
        result_msg = "FileNotFoundError - Failed to read Member DB file"

    # 문제 DB 마지막 업데이트 시간
    try:
        with open('./data/solved-db.json', 'r', encoding='utf-8') as f:
            solved_db = json.load(f)
            result_obj['problem_last_udt'] = solved_db['last_update_time']
    except FileNotFoundError:
        logger.debug("Failed to read Solved DB file")
        result_msg = "FileNotFoundError - Failed to read Solved DB file"
    finally:

        result_obj['result_msg'] = result_msg

    return result_obj
