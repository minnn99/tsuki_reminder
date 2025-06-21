from linebot import LineBotApi
from linebot.models import TextSendMessage
import schedule
import time

# 방금 발급받은 토큰
line_bot_api = LineBotApi("V5vclVKBXE+iNPX8MuMI9P36AKZdVWiNF2VSXMiCHz1L4N5QBw7N19c9oCIQcAMl8yRFF0jxtKo7ME2T25rsk8ngc0qmI0GANDWs6JnOcMfQM/HaZCBtjQlLvyZfO+VCP8UYdXQKrSq+XWTgXtXIJgdB04t89/1O/w1cDnyilFU=")

def send_reminder():
    try:
        line_bot_api.broadcast(TextSendMessage(text="💊약 먹을 시간이야 자기~~오늘도 수고 많았어 사랑해❤️"))
        print(f"메시지 전송 성공: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"메시지 전송 실패: {str(e)}")

# 매일 저녁 8:50에 실행되도록 설정
schedule.every().day.at("20:50").do(send_reminder)

# 프로그램을 계속 실행하면서 스케줄 체크
print("리마인더 봇이 실행되었습니다. 매일 저녁 8:50에 메시지를 전송합니다.")
print("프로그램을 종료하려면 Ctrl+C를 누르세요.")

while True:
    schedule.run_pending()
    time.sleep(1)
