import telebot
import requests

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота
TOKEN = '7292337703:AAFxTZHEH5QCCvgVECeIcdxSZKfjfQsZu-w'
bot = telebot.TeleBot(TOKEN)

API_KEY = 'E99l9NOctud3vmu6bPne'
FLUXUS_URL_PREFIX = "https://flux.li/android/external/start.php?HWID="
DELTA_URL_PREFIX = "https://gateway.platoboost.com/a/8?id="

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    hwid = message.text
    if hwid.startswith(FLUXUS_URL_PREFIX):
        hwid = hwid[len(FLUXUS_URL_PREFIX):]
        url_fluxus = f"https://stickx.top/api-fluxus/?hwid={hwid}&api_key={API_KEY}"
        response_fluxus = requests.get(url_fluxus)
        
        if response_fluxus.status_code == 200:
            fluxus = response_fluxus.json()
            key_fluxus = fluxus.get('key', 'No key found')
            response_message_fluxus = (
                "🌟 *FLUXUS* 🌟\n\n"
                f"🔓 *Key*\n`{key_fluxus}`\n\n"
                "CapyExBot 🗂"
            )
            bot.reply_to(message, response_message_fluxus, parse_mode="MarkdownV2")
        else:
            bot.reply_to(message, "❌ _Fail_", parse_mode="MarkdownV2")
    
    elif hwid.startswith(DELTA_URL_PREFIX):
        hwid = hwid[len(DELTA_URL_PREFIX):]
        url_delta = f"https://stickx.top/api-delta/?hwid={hwid}&api_key={API_KEY}"
        response_delta = requests.get(url_delta)
        
        if response_delta.status_code == 200:
            delta = response_delta.json()
            key_delta = delta.get('key', 'No key found')
            response_message_delta = (
                "🔰 *DELTA* 🔰\n\n"
                f"🔓 *Key*\n`{key_delta}`\n\n"
                "CapyExBot 🗂"
            )
            bot.reply_to(message, response_message_delta, parse_mode="MarkdownV2")
        else:
            bot.reply_to(message, "❌ _Fail_", parse_mode="MarkdownV2")
    else:
        bot.reply_to(message, "❌ _Invalid URL_", parse_mode="MarkdownV2")

if __name__ == "__main__":
    import threading
    import time

    def start_bot():
        bot.polling()

    def handle_input():
        while True:
            hwid = input("You Hwid: ")
            if hwid.startswith(FLUXUS_URL_PREFIX):
                hwid = hwid[len(FLUXUS_URL_PREFIX):]
                url_fluxus = f"https://stickx.top/api-fluxus/?hwid={hwid}&api_key={API_KEY}"
                
                response_fluxus = requests.get(url_fluxus)
                if response_fluxus.status_code == 200:
                    fluxus = response_fluxus.json()
                    key_fluxus = fluxus.get('key', 'No key found')
                    print(
                        "🌟 FLUXUS 🌟\n\n"
                        f"🔓 Key\n\n"
                        f"{key_fluxus}\n\n"
                        "CapyExBot🗂"
                    )
                else:
                    print("\nFail\n")
            elif hwid.startswith(DELTA_URL_PREFIX):
                hwid = hwid[len(DELTA_URL_PREFIX):]
                url_delta = f"https://stickx.top/api-delta/?hwid={hwid}&api_key={API_KEY}"
                
                response_delta = requests.get(url_delta)
                if response_delta.status_code == 200:
                    delta = response_delta.json()
                    key_delta = delta.get('key', 'No key found')
                    print(
                        "🔰 DELTA 🔰\n\n"
                        f"🔓 Key\n\n"
                        f"{key_delta}\n\n"
                        "CapyExBot🗂"
                    )
                else:
                    print("\nFail\n")
            else:
                print("\nInvalid URL\n")

    bot_thread = threading.Thread(target=start_bot)
    input_thread = threading.Thread(target=handle_input)

    bot_thread.start()
    input_thread.start()

    bot_thread.join()
    input_thread.join()
