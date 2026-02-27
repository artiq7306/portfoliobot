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
# Botni kodlari

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}! 👋\n\n"
        "Artiqbayning shaxsiy botiga xush kelibsiz.\n"
        "Xabar qoldirish uchun pastdagi \"Portfolio\" tugmasini bosing yoki shu botga yozing 🚀."
    )

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}! 👋\n\n"
        "Artiqbayning shaxsiy botiga xush kelibsiz.\n"
        "Xabar qoldirish uchun pastdagi \"Portfolio\" tugmasini bosing yoki shu botga yozing 🚀."
    )

# Har qanday boshqa matnli xabarga avto-javob
@dp.message()
async def auto_reply(message: types.Message):
    await message.answer(
        "Xabaringiz qabul qildim. ✅\n"
        "Tez orada javob beraman!"
    )


# ======================================
#  Botni va Serverni ishga tushrsh

def run_bot():
    bot.polling(non_stop=True)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=5000, debug=True)
