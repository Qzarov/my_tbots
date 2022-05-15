import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN_BUTTONS)
num = 0

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Надо написать статью...")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Чем планируешь заняться?".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Надо написать статью..." \
            or message.text == "Ну мааам..." \
            or message.text == "Ладно, иду делать..."\
            or message.text == "Пройти мимо":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прокрастинировать...")
        btn2 = types.KeyboardButton("Искать материалы")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Что будешь делать?)", reply_markup=markup)
    elif message.text == "Прокрастинировать...":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("5 минут")
        btn2 = types.KeyboardButton("1 час")
        btn3 = types.KeyboardButton("Начну завтра)")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="И сколько будем прокрастинировать?", reply_markup=markup)

    elif message.text == "5 минут" \
            or message.text == "1 час" \
            or message.text == "Начну завтра)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Ну мааам...")
        btn2 = types.KeyboardButton("Ладно, иду делать...")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="А чего не с понедельника?", reply_markup=markup)

    elif message.text == "Искать материалы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Платные базы")
        button2 = types.KeyboardButton("Интернет")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Где будем искать?", reply_markup=markup)

    elif message.text == "Платные базы" or message.text == "Интернет":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Искать материалы")
        button2 = types.KeyboardButton("Как же надоело!!1!")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Несколько часов спустя...")
        bot.send_message(message.chat.id, text="Ты почти у цели!", reply_markup=markup)

    elif message.text == "Как же надоело!!1!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("DeScienz Platform")
        markup.add(button1)
        bot.send_message(message.chat.id,
                         text="В красках рассказывая другу о том, что "
                              "толкового ничего не найти, ты натыкаешься на...",
                         reply_markup=markup)

    elif message.text == "DeScienz Platform":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Пройти мимо")
        button2 = types.KeyboardButton("Опа! Что это?")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Хм...", reply_markup=markup)

    elif message.text == "Опа! Что это?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Стать супер-пупер-учёным")
        markup.add(button1)
        bot.send_message(message.chat.id,
                         text="Это "
                              "супер-пупер "
                              "платформа!",
                         reply_markup=markup)

    elif message.text == "Стать супер-пупер-учёным":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Главное - не останавливаться на достигнутом")
        markup.add(button1)
        bot.send_message(message.chat.id,
                         text="Ура! Теперь у тебя есть вся нужная информация "
                         "и ты пишешь статью, которую тут же публикуют!",
                         reply_markup=markup)

    elif message.text == "Главное - не останавливаться на достигнутом":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Надо написать статью...")
        markup.add(button1)
        bot.send_message(message.chat.id, text="Ты к успеху шел...")
        bot.send_message(message.chat.id, text="И дошел!")
        bot.send_message(message.chat.id, text="Поздравляем!", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text="Я тебя не понимаю, человек...")


bot.polling(none_stop=True)
