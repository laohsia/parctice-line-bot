from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('pyUQ4+W00FKdp1BE2gwVN/sU65uS9NLcqKx4qI5d7hGRBgybpTJZEt7zpDdnkdztbN6aREBv+VqtKgZxx3qhVUsmL5J4E1ie+Rn9iLRqWm+83pHXq4iF0thk5NEQGbYTi5X5zUDB1IK7o0zHykqsEgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('de5270aba4e2a5ffd32b2853c46601cd')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    re = "超出回覆範圍，請重新輸入"

    if msg in ["哈囉","hi","Hi","HI","你好","妳好"] :
        re = "你好~很高興認識你，請在下列關鍵字中選擇您想聊天的話題並輸入關鍵字: 交友"
    elif msg == "交友":
        re = "是不是碰到什麼困難了呢?"
        sticker_message = StickerSendMessage(
            package_id = "11537" ,
            sticker_id = "52002744"
            )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
    elif "吵架" in msg:
        re = "吵架是在所難免的啦~是因為在乎你/妳才會這樣的~"
    elif "體重" in msg:
        re = "多多運動以及均衡飲食，保持健康的體態是很重要的!"
    elif "價值觀" in msg:
        re = "這種事情只需要雙方冷靜下來多多溝通就沒問題~"
    elif "分手" in msg:
        re = "先冷靜下來想想看，千萬別衝動行事"
    elif "家人" in msg:
        re = "家人跟伴侶都非常重要，所以你必須扮演好潤滑的角色!"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=re))


if __name__ == "__main__":
    app.run()
