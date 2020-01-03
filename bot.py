import time
import parseVK
import api
import config


while True:
    post_id = parseVK.get_latest_post()["id"]
    f = open('latestPosted')
    latestPosted = int(f.read())
    f.close()
    if post_id == latestPosted:
        time.sleep(60)
    else:
        post = "wall" + str(config.CHGK_VK_ID) + "_" + str(post_id)
        f = open('weeklyText.txt')
        api.send_message(f.read(), attachments=[post])
        f.close()
        f = open('latestPosted', 'w')
        f.write(str(post_id))
        f.close()
