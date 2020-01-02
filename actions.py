import json
import config
import api


def send_poll(question, answers, message=""):
    poll = api.create_poll(question, answers)
    poll = json.loads(poll)
    pollID = str(poll["response"]["id"])
    to_attach = "poll" + str(config.GROUP_ID) + "_" + pollID
    response = api.send_message(message, attachments=[to_attach])
    response["pollID"] = pollID
    return response
