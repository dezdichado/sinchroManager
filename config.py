import os
try:
    import secret_config
except ImportError:
    secret_config = None


def secret(var_name):
    if secret_config is None:
        return None
    else:
        try:
            return getattr(secret_config, var_name)
        except AttributeError:
            return None


def get_config(var_name):
    return os.getenv(var_name, secret(var_name))


ACCESS_TOKEN = get_config('ACCESS_TOKEN')
USER_TOKEN = get_config('USER_TOKEN')
SERVICE_TOKEN = get_config('SERVICE_TOKEN')
DIFFICHENTO_ID = 2000000000 + 1
GROUP_ID = -184645364
CHGK_VK_ID = -89780700
WEEKEND_HASHTAG = "#ЧГК_синхроны_уикэнда"
