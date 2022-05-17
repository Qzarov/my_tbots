import random

import telebot
from telebot import types
import config
import resourсes.stickers_and_text as res

bot = telebot.TeleBot(config.TOKEN_DESCIENZ)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Надо написать статью...")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="{0.first_name}, команда DeScienz тебя категорически приветствует!\n"
                          "Больше информации по команде /help".format(message.from_user))
    bot.send_sticker(message.chat.id, res.get_rand_stic_id(res.hi_stics))
    bot.send_message(message.chat.id,
                     text="Чем планируешь заняться?"
                     .format(message.from_user), reply_markup=markup)

    bot.send_message(config.my_id,
                     text="{0.first_name} {0.last_name} (@{0.username}) пишет. Мне страшно..."
                     .format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id,
                     text=res.bot_info.format(message.from_user))


def set_buttonz(btn1, btn2="", btn3=""):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if btn2 == "":
        markup.add(btn1)
    elif btn3 == "":
        markup.add(btn1, btn2)
    else:
        markup.add(btn1, btn2, btn3)

    return markup


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Надо написать статью..." \
            or message.text == "Ну мааам..." \
            or message.text == "Ладно, иду делать..."\
            or message.text == "Пройти мимо":
        bot.send_message(message.chat.id,
                         text="Что будешь делать?)",
                         reply_markup=set_buttonz("Прокрастинировать...", "Искать материалы"))

    elif message.text == "Прокрастинировать...":
        bot.send_message(message.chat.id,
                         text="И сколько будем прокрастинировать?",
                         reply_markup=set_buttonz("5 минут", "1 час", "Начну завтра)"))
        bot.send_sticker(message.chat.id, res.get_rand_stic_id(res.thinking_stics))

    elif message.text == "5 минут" \
            or message.text == "1 час" \
            or message.text == "Начну завтра)":
        bot.send_message(message.chat.id,
                         text="А чего не с понедельника?",
                         reply_markup=set_buttonz("Ну мааам...", "Ладно, иду делать..."))

    elif message.text == "Искать материалы":
        bot.send_message(message.chat.id,
                         text="Где будем искать?",
                         reply_markup=set_buttonz("Платные базы", "Интернет"))

    elif message.text == "Платные базы" or message.text == "Интернет":
        bot.send_message(message.chat.id, text="Несколько часов спустя...")
        bot.send_sticker(message.chat.id, res.get_rand_stic_id(res.keep_it_up_stics))
        bot.send_message(message.chat.id,
                         text="Ты почти у цели!",
                         reply_markup=set_buttonz("Искать материалы", "Как же надоело!!1!"))

    elif message.text == "Как же надоело!!1!":
        bot.send_message(message.chat.id,
                         text="В красках рассказывая другу о том, что "
                              "толкового ничего не найти, ты натыкаешься на...",
                         reply_markup=set_buttonz("DeScienz Platform"))

    elif message.text == "DeScienz Platform":
        bot.send_message(message.chat.id,
                         text="Хм...",
                         reply_markup=set_buttonz("Пройти мимо", "Опа! Что это?"))

    elif message.text == "Опа! Что это?":
        bot.send_message(message.chat.id,
                         text="Это "
                              "супер-пупер "
                              "платформа для поиска научных статей!",
                         reply_markup=set_buttonz("Стать супер-пупер-учёным"))
        bot.send_sticker(message.chat.id, res.get_rand_stic_id(res.love_it_stics))

    elif message.text == "Стать супер-пупер-учёным":

        bot.send_message(message.chat.id,
                         text="Ура! Теперь у тебя есть вся нужная информация "
                         "и ты пишешь статью, которую тут же публикуют!",
                         reply_markup=set_buttonz("Главное - не останавливаться на достигнутом"))
        bot.send_sticker(message.chat.id, res.get_rand_stic_id(res.congrats_stics))

    elif message.text == "Главное - не останавливаться на достигнутом":
        bot.send_message(message.chat.id, text="Ты к успеху шел...")
        bot.send_message(message.chat.id, text="И дошел!")
        bot.send_message(message.chat.id,
                         text="Публикуйся и да публикуем будешь!",
                         reply_markup=set_buttonz("Надо написать статью..."))
        file = open(res.uchoniy_pic[random.randint(0, 1)], 'rb')
        bot.send_photo(message.chat.id, file)

    else:
        bot.send_message(message.chat.id, text="Человек, я тебя не понимаю 🤨")


bot.polling(none_stop=True)
