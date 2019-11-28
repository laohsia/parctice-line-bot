import requests
import json

headers = {"Authorization":"Bearer pyUQ4+W00FKdp1BE2gwVN/sU65uS9NLcqKx4qI5d7hGRBgybpTJZEt7zpDdnkdztbN6aREBv+VqtKgZxx3qhVUsmL5J4E1ie+Rn9iLRqWm+83pHXq4iF0thk5NEQGbYTi5X5zUDB1IK7o0zHykqsEgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "Controller",
    "areas":[
        {
          "bounds": {"x": 551, "y": 325, "width": 321, "height": 321},
          "action": {"type": "message", "text": "up"}
        },
        {
          "bounds": {"x": 876, "y": 651, "width": 321, "height": 321},
          "action": {"type": "message", "text": "right"}
        },
        {
          "bounds": {"x": 551, "y": 972, "width": 321, "height": 321},
          "action": {"type": "message", "text": "down"}
        },
        {
          "bounds": {"x": 225, "y": 651, "width": 321, "height": 321},
          "action": {"type": "message", "text": "left"}
        },
        {
          "bounds": {"x": 1433, "y": 657, "width": 367, "height": 367},
          "action": {"type": "message", "text": "btn b"}
        },
        {
          "bounds": {"x": 1907, "y": 657, "width": 367, "height": 367},
          "action": {"type": "message", "text": "btn a"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)
