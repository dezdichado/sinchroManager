import json
import api
import config
import datetime


def get_latest_post():
    posts = api.search_wall(config.CHGK_VK_ID, config.WEEKEND_HASHTAG, count=1, offset=0)
    posts = json.loads(posts)
    return posts["response"]["items"][0]
