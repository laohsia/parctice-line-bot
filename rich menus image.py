from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('pyUQ4+W00FKdp1BE2gwVN/sU65uS9NLcqKx4qI5d7hGRBgybpTJZEt7zpDdnkdztbN6aREBv+VqtKgZxx3qhVUsmL5J4E1ie+Rn9iLRqWm+83pHXq4iF0thk5NEQGbYTi5X5zUDB1IK7o0zHykqsEgdB04t89/1O/w1cDnyilFU=')

with open("control-1.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-d4526097438a7afe7d3b0d6ca01825d6", "image/jpeg", f)
