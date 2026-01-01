import telebot
from telebot import types
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# سيرفر وهمي لتجنب إغلاق Render للبوت
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'SHADOW SYSTEM IS ONLINE')

def run_server():
    port = int(os.environ.get('PORT', 8080))
    httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()

# ضع التوكن الخاص بك هنا
TOKEN = '8468154462:AAHkVqMSAqxBQ6iq-TaSYSVH3B-rZkyQKD8'
bot = telebot.TeleBot(TOKEN)

# دالة إنشاء الأزرار الاحترافية
def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btns = [
        '📸 اختراق الكاميرا', '📍 اختراق الموقع',
        '💳 صيد فيزات', '📱 اختراق تيك توك',
        '👤 اختراق فيسبوك', '📸 اختراق انستقرام',
        '🛡️ فحص رابط', '📡 معلومات IP',
        '🎤 تسجيل صوت', '🚫 إغلاق مواقع'
    ]
    markup.add(*(types.KeyboardButton(b) for b in btns))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (
        "Welcome to **SHΔDØW CØRE V2** 💀\n\n"
        "الآن يمكنك التحكم الكامل والوصول للثغرات المتاحة."
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu(), parse_mode='Markdown')

@bot.message_handler(func=lambda m: True)
def handle_commands(message):
    responses = {
        '📸 اختراق الكاميرا': "📸 جاري إنشاء رابط سحب الصور.. أرسله للضحية.",
        '📍 اختراق الموقع': "📍 جاري توليد رابط GPS لسحب الإحداثيات..",
        '💳 صيد فيزات': "💳 تم تفعيل صفحة التصيد للبطاقات البنكية.. بانتظار اللوجات.",
        '📱 اختراق تيك توك': "📱 أدخل يوزر الحساب المستهدف لبدء الهجوم.."
    }
    
    msg = responses.get(message.text, "⚙️ جاري معالجة الطلب في السيرفر السحابي..")
    bot.reply_to(message, msg)

if __name__ == "__main__":
    threading.Thread(target=run_server).start()
    bot.polling(none_stop=True)
