import os
import sys
import urllib.request
import json

def get_translate2(text):

    client_id = "eD7mcxCLoKI7Og4K1AJ0" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "K8EGRFWDQb" # 개발자센터에서 발급받은 Client Secret 값

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

