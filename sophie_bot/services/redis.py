import sys
from redis import Redis
import redis as redis_lib
from sophie_bot import log
from sophie_bot.config import get_str_key, get_int_key, get_bool_key

if get_bool_key("HEROKU") is True:
    redis = redis_lib.Redis(
        host=get_str_key("REDIS_URI"),
        port=get_str_key("REDIS_PORT"),
        password=get_str_key("REDIS_PASS"),
        decode_responses=True
    )

    bredis = redis_lib.Redis(
        host=get_str_key("REDIS_URI"),
        port=get_str_key("REDIS_PORT"),
        password=get_str_key("REDIS_PASS"),
    )

if get_bool_key("HEROKU") is False:
    redis = redis_lib.StrictRedis(
        host=get_str_key("REDIS_URI"),
        port=get_str_key("REDIS_PORT"),
        db=get_int_key("REDIS_DB_FSM"),
        decode_responses=True
    )

    bredis = redis_lib.StrictRedis(
        host=get_str_key("REDIS_URI"),
        port=get_str_key("REDIS_PORT"),
        db=get_int_key("REDIS_DB_FSM")
    )

