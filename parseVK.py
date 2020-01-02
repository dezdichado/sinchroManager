import json
import api
import config
import datetime


def get_latest_post():
    temp_offset = (int(datetime.datetime.timestamp(datetime.datetime.now())) // 60) % 30
    posts = api.search_wall(config.CHGK_VK_ID, config.WEEKEND_HASHTAG, count=1, offset=temp_offset)
    posts = json.loads(posts)
    return posts["response"]["items"][0]
