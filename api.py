import urllib.request, urllib.parse
import ssl
import time
import config


def call_method(name, params):
    '''
    :param name: str
    :param params: dict
    :return: str
    '''
    paramStrings = [key + "=" + urllib.parse.quote(str(params[key])) for key in params]
    token = config.ACCESS_TOKEN
    basicUrl = "https://api.vk.com/method/"

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = basicUrl + name + "?" + "&".join(paramStrings) + "&access_token=" + token + "&v=" + "5.101"
    response = urllib.request.urlopen(url, context=ctx).read().decode()
    return response

def send_text(text):
    method = "messages.send"
    params = {
        "peer_id": config.DIFFICHENTO_ID,
        "message": text,
        "random_id": time.time()
    }

    return call_method(method, params)

