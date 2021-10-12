import os
import sys
import urllib.request
import json

def get_translate2(text):

    client_id = "" # 
    client_secret = "" # 파파고 번역 api key

    encText = urllib.parse.quote(text)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
        return result
    else:
        print("Error Code:" + rescode)

