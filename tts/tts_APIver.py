import requests
from urllib.parse import urlencode

API_KEY = "xIKgCA65Nkr1uT781juhP8fV"
SECRET_KEY = "tYnMoFH4yFvhLQnTs955p9M2TxwNvRZL"

CUID = "b0:be:83:81:83:1b"

path = './tts/temp/tempvoice.wav' #path of raw_wav tempfile

def tts_api(token, text):
        
    url = "https://tsn.baidu.com/text2audio"
    
    params = {
        'tex':text,
        'lan':'zh',
        'cuid':CUID,
        'ctp':1,
        'tok':token,
        'per':4,
        'pit':6
    }

    para = urlencode(params, encoding='utf-8')

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*'
    }
    
    response = requests.request("GET", url, headers=headers, params=params)

    with open(path, 'wb') as f:
        f.write(response.content)
    



def get_access_token():

    """
    使用 AK,SK 生成鉴权签名(Access Token)
    :return: access_token,或是None(如果错误)
    """

    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    token =  str(requests.post(url, params=params).json().get("access_token"))
    print("token:", token)
    return str(token)




