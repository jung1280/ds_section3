import requests

def get_translate(text):
    client_id = "eD7mcxCLoKI7Og4K1AJ0"
    client_secret = "K8EGRFWDQb"

    data = {'text' : text,
            'source' : 'ko',
            'target': 'en'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])

        return trans_data

    else:
        print("Error Code:" , rescode)

