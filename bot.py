import time
import parseVK
import api
import config


while True:
    post_id = parseVK.get_latest_post()["id"]
    latestPosted = int(open('latestPosted').read())
    if post_id == latestPosted:
        time.sleep(60)
    else:
        post = "wall" + str(config.CHGK_VK_ID) + "_" + str(post_id)
        api.send_message("Появилось расписание синхронов на следующую неделю!", attachments=[post])
        open('latestPosted', 'w').write(str(post_id))
