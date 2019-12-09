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

    if "貼圖" in msg:
        sticker_message = StickerSendMessage(
            package_id = "11537" ,
            sticker_id = "52002744"
            )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return
    
    elif "找工作" in msg :
        re = "你好~很高興認識你，感謝您加職缺小幫手為您的好友!\n小幫手為您快速搜尋符合專業的職缺，請在下列選單中點選您所需要的選項。\n由左至右分別為學生、新鮮人、上班族，請依身分選擇，系統會導向對應的求職頁面!\n假如沒有符合的選項，請輸入[不符合身分]"
    elif "不符合身分" in msg:
        re = "請稍等，軟體更新功能中"
        
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=re))


if __name__ == "__main__":
    app.run()
