from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('TXYoK/14QdxIhp+FQigL123CABlNjVGHxPGBZIvEBjdd8H+KKx2Yo9NqFWp/m/ITwVREZICaFClZYRHtd6cN/OnGKqst9vwUTyKZAEFR6JZ70CkQwblFydxzw2blNxsUOaLAlCcqrT7XJ1eA+lhB6QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ee5f681e7c41dc0af485d70b80a1b382')


@app.route("/callback", methods=['POST'] 
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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
