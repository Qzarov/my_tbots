import telebot
import sqlite3
import config

#bot
bot = telebot.TeleBot(config.TOKEN_FILTER_BOT)

@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER
    )""")

    connect.commit()

    #add values in fields
    user_id = [message.chat.id]
    cursor.execute("INSERT INTO users VALUES(?);", user_id)

    bot.send_message(message.chat.id, text="Я тебя записал!".format(message.from_user))

# polling
bot.polling()