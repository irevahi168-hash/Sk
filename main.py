import telebot
from telebot import types
from flask import Flask
import threading
import os

# আপনার বোট টোকেন এবং লিভব্রিারি সেটআপ
API_TOKEN = '8566511093:AAHZb6AyZ-f6dRRxWXWUuLCWh4Z6wY7hEBI'
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

# Render-এ পোর্ট ডিটেক্ট করার জন্য
PORT = int(os.environ.get('PORT', 8080))

@server.route("/")
def webhook():
    return "Bot is Alive!", 200

# /start কমান্ড
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # আপনার চ্যানেলের লিঙ্ক দিন
    btn_join = types.InlineKeyboardButton("📢 Join Channel", url="https://t.me/your_channel")
    
    # আপনার ওয়েবসাইটের লিঙ্ক দিন
    web_app = types.WebAppInfo(url="https://tndx.fun")
    btn_web = types.InlineKeyboardButton("🌐 Open Website", web_app=web_app)
    
    markup.add(btn_join, btn_web)
    
    bot.send_message(message.chat.id, f"স্বাগতম {message.from_user.first_name}!\nওয়েবসাইট ওপেন করতে নিচের বাটনে ক্লিক করুন।", reply_markup=markup)

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # বোটটি আলাদা থ্রেডে চালানো যাতে ফ্লস্ক সার্ভারও চালু থাকে
    threading.Thread(target=run_bot).start()
    server.run(host="0.0.0.0", port=PORT)
