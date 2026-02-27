from flask import Flask
import threading
import telebot

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "salom bot ishlayapti", 200

# ======================================
# BOT
TOKEN = "8254250258:AAG8mRx9gVzVAROzymAsbfykT2IGds9HR2I"

bot = telebot.TeleBot(TOKEN)

# ======================================
# Bot kodlari (Fixed for telebot)

# Start komandasi uchun
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.reply_to(
        message,
        f"Assalomu alaykum, {message.from_user.full_name}! 👋\n\n"
        "Artiqbayning shaxsiy botiga xush kelibsiz.\n"
        "Xabar qoldirish uchun pastdagi \"Portfolio\" tugmasini bosing yoki shu botga yozing 🚀."
    )

# Har qanday boshqa matnli xabarga avto-javob
@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    bot.send_message(
        message.chat.id,
        "Xabaringiz qabul qildim. ✅\n"
        "Tez orada javob beraman!"
    )

# ======================================
# Botni va Serverni ishga tushirish

def run_bot():
    # non_stop=True keeps the bot running even if an error occurs
    bot.infinity_polling()

if __name__ == "__main__":
    # Run bot in a separate thread so Flask can run simultaneously
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
