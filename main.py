import telebot
import google.generativeai as genai
import time
from flask import Flask
from threading import Thread

# Калитларингиз
TOKEN = "8266465743:AAFzRTTm8bAzybSnfW3EPMdr_Ge-IuJq1WE"
AI_KEY = "AIzaSyCAT8tfd2AeKUGV-nlLDEj7mxssK14ebyc"

bot = telebot.TeleBot(TOKEN)
genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Серверни уйғоқ тутиш учун (Render учун)
app = Flask('')
@app.route('/')
def home(): return "Бот тирик!"
def run(): app.run(host='0.0.0.0', port=8080)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ Nazarov AI боти фаол! График юборинг.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        # Расмни олиш ва AI га юбориш қисми
        bot.reply_to(message, "⏳ Таҳлил кетмоқда...")
        # (Бу ерда AI таҳлил логикаси бўлади)
    except Exception as e:
        bot.reply_to(message, f"❌ Хатолик: {e}")

if __name__ == "__main__":
    Thread(target=run).start()
    bot.polling(none_stop=True)
