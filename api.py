import urllib.request, urllib.parse
import ssl
import time
import config


def call_method(name, params, token=config.ACCESS_TOKEN):
    '''
    :param name: str
    :param params: dict
    :return: str
    '''
    paramStrings = [key + "=" + urllib.parse.quote(str(params[key])) for key in params]
    basicUrl = "https://api.vk.com/method/"

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = basicUrl + name + "?" + "&".join(paramStrings) + "&access_token=" + token + "&v=" + "5.101"
    response = urllib.request.urlopen(url, context=ctx).read().decode()
    return response


def send_message(text, attachments=None):
    method = "messages.send"
    params = {
        "peer_id": config.DIFFICHENTO_ID,
        "message": text,
        "random_id": time.time(),
    }
    if attachments is not None:
        params["attachment"] = ','.join(attachments)

    return call_method(method, params)


def create_poll(question, answers, is_anonymous=0, is_multiple=1, end_date=-1,
                background_id=1):
    '''
    :param question: str
    :param answers: list
    :return: str
    '''
    method = "polls.create"
    params = {
        "question": question,
        "add_answers": str(answers).replace("'", '"'),
        "is_anonymous": is_anonymous,
        "is_multiple": is_multiple,
        "background_id": background_id,
        "owner_id": config.GROUP_ID
    }
    if end_date >= 1558003357:
        params["end_date"] = end_date

    return call_method(method, params, token=config.USER_TOKEN)
