from requests import *

import os, json, datetime

def GPT(InPut):

  api = "https://gpt.chatapi.art/backend-api/conversation"

  headers = {

    "authority": "gpt.chatapi.art",

    "method": "POST",

    "path": "/backend-api/conversation",

    "scheme": "https",

    "accept": "text/event-stream",

    "accept-encoding": "gzip, deflate, br",

    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",

    "authorization": "Bearer",

    "content-length": "236",

    "content-type": "application/json",

    "origin": "https://gpt.chatapi.art",

    "referer": "https://gpt.chatapi.art/",

    "sec-ch-ua": """Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108""",

    "sec-ch-ua-mobile": "?0",

    "sec-ch-ua-platform": "Windows",

    "sec-fetch-dest": "empty",

    "sec-fetch-mode": "cors",

    "sec-fetch-site": "same-origin",

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42",

    "If-Modified-Since": f"Tue, 28 Jan 2020 12:{datetime.datetime.now().minute}:{datetime.datetime.now().second} GMT",

  }

  Json = {"action": "next",

        "messages": [{"id": "a2e292a1-59cc-4fca-81ed-5a8f8458f1be",

                      "role": "user",

                      "content": {"content_type": "text", "parts": [InPut]}}],

        "parent_message_id": "be81a331-eacf-45fd-bc47-6a6375ab2335",

        "model": "text-davinci-002-render"}

  RES = ""

  data = post(api, json=Json, headers=headers).text.replace("data: ", "")

  lis0 = data.split("\n")

  for i in lis0[::-1]:

    if i and i != '[DONE]':

        RES = i

        break

  try:

    Res = json.loads(RES)['message']['content']['parts'][0]

  except:

    print("Error:",RES)

    print("处理字典数据时发生错误.")

    Res="[Error]"

  return Res