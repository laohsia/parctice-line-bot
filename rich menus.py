import requests
import json

headers = {"Authorization":"Bearer pyUQ4+W00FKdp1BE2gwVN/sU65uS9NLcqKx4qI5d7hGRBgybpTJZEt7zpDdnkdztbN6aREBv+VqtKgZxx3qhVUsmL5J4E1ie+Rn9iLRqWm+83pHXq4iF0thk5NEQGbYTi5X5zUDB1IK7o0zHykqsEgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 843},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "Controller",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 833, "height": 843},
          "action": {"type": "uri","label": "Studnet","uri":"https://www.104.com.tw/area/student/index.cfm"}
        },
        {
          "bounds": {"x": 833, "y": 0, "width": 833, "height": 843},
          "action": {"type": "uri","label": "Fresh men","uri":"https://www.104.com.tw/area/freshman/main/index"}
        },
        {
          "bounds": {"x": 1666, "y": 0, "width": 833, "height": 843},
          "action": {"type": "uri","label": "Office worker","uri":"https://www.104.com.tw/area/cj/"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)
