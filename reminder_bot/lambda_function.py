from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

def lambda_handler(event, context):
    LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
    line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
    
    try:
        line_bot_api.broadcast(TextSendMessage(text="💊약 먹을 시간이야 자기~~오늘도 수고 많았어 사랑해❤️"))
        return {
            'statusCode': 200,
            'body': '메시지 전송 성공'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'메시지 전송 실패: {str(e)}'
        }