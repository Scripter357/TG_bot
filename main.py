import telebot
from telebot import types
import requests
tokenFile = open("token", 'r')
token = tokenFile.readline().rstrip()

bot = telebot.TeleBot(token)
x = bot.get_me()
print(x)



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "нет", "кто автор?", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\n /whats2by2 - тест 2+2\n /randomsite - случайный сайт в Сети\n /somethingtoread - случайная страница википедии\n')


@bot.message_handler(commands=['whats2by2'])
def start_message(message):
    bot.send_message(message.chat.id, '4')

@bot.message_handler(commands=['randomsite'])
def start_message(message):
    bot.send_message(message.chat.id, 'Got it.')
    bot.send_message(message.chat.id, "https://therandombutton.github.io/random.html")

@bot.message_handler(commands=['somethingtoread'])
def start_message(message):
    bot.send_message(message.chat.id, 'Alright.')
    random_article = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    bot.send_message(message.chat.id, random_article.url)



@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if message.text.lower() == "нет":
        bot.send_message(message.chat.id, 'Ну ладно :/')
    if message.text.lower() == "кто автор?":
        bot.send_message(message.chat.id, 'Павел из БВТ2108')

bot.polling()
