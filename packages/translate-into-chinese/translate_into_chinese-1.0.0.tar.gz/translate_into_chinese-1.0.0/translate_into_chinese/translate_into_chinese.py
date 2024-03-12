# -*- coding: utf-8 -*-
import hashlib
import random
import requests

#http://api.fanyi.baidu.com/doc/21

def translate_into_chinese(q):
    appid = '20220712001270949'
    secret_key = 'ODwtPobgXFes3sBML_NM'
    salt = str(random.randint(1000000000, 9999999999))
    m = hashlib.md5()
    m.update((appid + q + salt + secret_key).encode("utf8"))
    s = f'http://api.fanyi.baidu.com/api/trans/vip/translate?q={q}&from=auto&to=zh&appid={appid}&salt={salt}&sign={m.hexdigest()}'
    result = requests.get(s).json()
    return result["trans_result"][0]['dst']