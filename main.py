import telebot
from telebot import types
import requests
token = "5035729554:AAHCIDSrzIeuXi8-s6DAjilyunU-AADHFYo"

bot = telebot.TeleBot(token)
x = bot.get_me()
print(x)



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\n- Тестовые команды: /whats2by2 /ignorethis /somethingtoread \n- Тестовые варианты: "хочу", "нет", "Кто автор?"')


@bot.message_handler(commands=['whats2by2'])
def start_message(message):
    bot.send_message(message.chat.id, '4')

@bot.message_handler(commands=['ignorethis'])
def start_message(message):
    bot.send_message(message.chat.id, 'OK')

@bot.message_handler(commands=['somethingtoread'])
def start_message(message):
    bot.send_message(message.chat.id, 'Alright.')
    random_article = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    bot.send_message(message.chat.id, random_article.url)



@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "нет":
        bot.send_message(message.chat.id, 'Ну ладно :/')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "кто автор?":
        bot.send_message(message.chat.id, 'Павел из БВТ2108')

bot.polling()
