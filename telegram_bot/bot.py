from telegram import Bot
from datetime import datetime, timedelta
import schedule
import time

# Токен вашего бота
BOT_TOKEN = "7773764245:AAEQbkMWAk7rKr7xR8xgRdcESQS-IJK0710"
# ID чата или группы
CHAT_ID = "-1001967275605"

# Функция для отправки голосования
def send_poll():
    bot = Bot(token=BOT_TOKEN)
    today = datetime.now()
    next_sunday = today + timedelta((6 - today.weekday()) % 7)
    game_date = next_sunday.strftime("%d.%m.%Y")
    question = f"Играем ли в воскресенье ({game_date}) в 21:30?"
    options = ["+", "-", "👀"]  # Варианты ответа
    bot.send_poll(
        chat_id=CHAT_ID,
        question=question,
        options=options,
        is_anonymous=False,  # Неанонимный опрос
        allows_multiple_answers=False
    )

# Настройка расписания
schedule.every().tuesday.at("14:00").do(send_poll)  # Опрос каждый вторник в 14:00

# Бесконечный цикл для выполнения задач по расписанию
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
