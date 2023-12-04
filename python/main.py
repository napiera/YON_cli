import requests
import json

API_HOST = 'http://58.232.146.242:50880'

def send_api(path, method, body):
    url = API_HOST + path
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    # body = {
    #     "key1": "value1":,
    #     "key2": "value2"
    # }

    print("")
    print("url %r" % url, " : %r" % method)
    
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))

        print("response status : %r" % response.status_code)
        json_response = json.loads(response.text)
        print("%r" % json_response)
    except Exception as ex:
        print(ex)
  

# 호출 예시
send_api('/api/user/1', 'GET', '')
send_api('/api/nation/user/1', 'GET', '')



peopel = {'nationId': 1, 'type': 'BASIC', 'properties': 'BASIC'}
send_api('/api/people/add', 'POST', peopel)


send_api('/api/nation/user/1', 'GET', '')

