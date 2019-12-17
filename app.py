from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage
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

    elif msg == "不符合身分" :
        buttons_template = ButtonsTemplate(
            title='其他職缺身分', text='請選擇以下身分別', actions=[
                URIAction(label='主管職', uri='https://www.104.com.tw/jobs/main/higher'),
                URIAction(label='中高齡', uri='https://senior.104.com.tw/?tabs=jobs&utm_source=official_104&utm_medium=104_menu_elderly'),

            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return

    elif msg == "image_carousel":
        image_carousel_template = ImageCarouselTemplate(columns=[
            ImageCarouselColumn(image_url='https://via.placeholder.com/1024x1024',
                                action=DatetimePickerAction(label='datetime',
                                                            data='datetime_postback',
                                                            mode='datetime')),
            ImageCarouselColumn(image_url='https://via.placeholder.com/1024x1024',
                                action=DatetimePickerAction(label='date',
                                                            data='date_postback',
                                                            mode='date'))
        ])
        template_message = TemplateSendMessage(
            alt_text='ImageCarousel alt text', template=image_carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return

    elif msg == "flex":
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(thumbnail_image_url='https://scontent.ftpe8-2.fna.fbcdn.net/v/t1.0-9/78858712_3020675774617584_8482206259481673728_n.jpg?_nc_cat=103&_nc_ohc=LcqCtsc9Mg4AQkWAfO3bHQkSFkQehfvv6JcB8Uph07V7mgieZ6G3k749w&_nc_ht=scontent.ftpe8-2.fna&oh=d0720b979ae3ae5e8164f4c3f7bcb2b1&oe=5E7D327A',
                           text='請填寫表單，完成後來電確認，取貨時付款即可', title='台中高鐵站門市(自取)',
                           actions=[
                URIAction(label='訂購表單', uri='https://bit.ly/2Lhgrnx'),
                MessageAction(label='門市地址', text='高鐵門市地址')
            ]),
            CarouselColumn(thumbnail_image_url='https://scontent.ftpe8-2.fna.fbcdn.net/v/t1.0-9/79327003_3020675734617588_111192146333138944_n.jpg?_nc_cat=103&_nc_ohc=TtWIs9eKc-sAQmpge1FFJnBDoRemxWS3a0-LVR6sHLhT35_mS8IKxTsXg&_nc_ht=scontent.ftpe8-2.fna&oh=27b81efab9bcbdf4f8d92525515d998b&oe=5EB39E9E',
                           text='請填寫表單，完成後來電確認，取貨時付款即可', title='美村門市(自取)',
                           actions=[
                URIAction(label='訂購表單', uri='https://bit.ly/2sAgS4I'),
                MessageAction(label='門市地址', text='美村本店地址')
            ]),
        ])
        template_message = TemplateSendMessage(
            alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        return

    if "找工作" in msg:
        re = "你好~很高興認識你，感謝您加職缺小幫手為您的好友!\n小幫手為您快速搜尋符合專業的職缺，請在下列選單中點選您所需要的選項。\n由左至右分別為學生、新鮮人、上班族，請依身分選擇，系統會導向對應的求職頁面!\n假如沒有符合的選項，請輸入[不符合身分]"
    elif "學生" in msg:
        re = "請輸入打工性質 :  長期、短期、假日、寒假、暑假"
    elif msg in ["長期","短期","假日","寒假","暑假"]:
        re = "請繼續輸入上班時段:\n日班、晚班、大夜班、假日班"
    elif msg in ["日班","晚班","大夜班","假日班"]:
        re = "請輸入欲工作地區"
        
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=re))


if __name__ == "__main__":
    app.run()
