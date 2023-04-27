import telebot
import requests

List = ['start', 'help' , "Komak" , "کمک"]
List2 = ["Nerkh" , "Qeimat Arz" , "نرخ ارز" , "قیمت ارز" ]

TOKEN = "5839723092:AAFp7nd6SZbPh6mvxWl01cjH_NxvgopRaPo"

bot = telebot.TeleBot(TOKEN)

URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"


@bot.message_handler(commands= List)
def send_welcome(message):
    bot.reply_to(message, "HI Im Amir What can i do for you ?")
@bot.message_handler(commands= List2)
def get_info(message):
    bot.reply_to(message , "Just Send Me The Currency \nLike : Btcusdt")

@bot.message_handler(func = lambda  m: True)
def show_price(message):
    symbol = message.text.upper()
    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    if response.status_code == 200 :
        data = response.json()
        print(data)
        bot.reply_to(message , f"{data['symbol']} price is {data['price']}")
    else :
        bot.reply_to(message , "Sth went wrong")

bot.infinity_polling()
