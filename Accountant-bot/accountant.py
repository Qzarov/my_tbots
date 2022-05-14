import sqlite3 as db

try:
    conn = db.connect("Accountant-bot/accountant.db")
    cursor = conn.cursor()

    # Cоздаем пользователя с user_id = 1000
    cursor.execute("INSERT INTO `users`(`user_id`) VALUES (?)", (1001,))

    # Считываем всех пользователей
    users = cursor.execute("SELECT * FROM `users`")
    print(users.fetchall())

    # Подтверждаем изменения
    conn.commit()

except db.Error as error:
    print("Error!", error)

finally:
    if(conn):
        conn.close()