import telebot
from telebot import types
from flask import Flask
import threading
import os

# আপনার বোট টোকেনটি এখানে দিন
API_TOKEN = '8766747501:AAEAUrdlqvh7t8zfo2yVKx1k8YZfCwRvlbY'
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

# Render-এ পোর্ট ডিটেক্ট করার জন্য
PORT = int(os.environ.get('PORT', 8080))

@server.route("/")
def webhook():
    return "Instagram Viral MMS Bot is running!", 200

# /start কমান্ড হ্যান্ডলার
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # আপনার ওয়েবসাইটের লিঙ্ক দিন (Web App হিসেবে ওপেন হবে)
    web_app = types.WebAppInfo(url="https://www.profitablecpmratenetwork.com/rc2k9c6yn?key=8be273d014468ed8e18810b9dcf1195e")
    btn_open = types.InlineKeyboardButton("🎬 Watch Now", web_app=web_app)
    
    # যদি আলাদা কোনো চ্যানেল জয়েন করাতে চান (ঐচ্ছিক)
    # btn_join = types.InlineKeyboardButton("📢 Join Update Channel", url="https://t.me/your_channel")
    
    markup.add(btn_open)
    
    # ইংরেজি ওয়েলকাম মেসেজ
    welcome_text = (
        f"Hello {message.from_user.first_name}!\n\n"
        "Welcome to **Instagram Viral MMS** Bot. 🔞\n"
        "Click the button below to watch viral mms videos."
    )
    
    bot.send_message(
        message.chat.id, 
        welcome_text, 
        reply_markup=markup, 
        parse_mode='Markdown'
    )

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # বোট এবং ফ্লস্ক সার্ভার একসাথে চালানো
    threading.Thread(target=run_bot).start()
    server.run(host="0.0.0.0", port=PORT)
    
