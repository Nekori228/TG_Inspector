import telebot

# Замените 'YOUR_BOT_TOKEN' на ваш токен, полученный от BotFather в Telegram
bot = telebot.TeleBot('5908947609:AAFn448qggrR0vky3C8q8ie68Gu0OltkKc4')

@bot.message_handler(commands=['get_username'])
def get_username(message):
    # Просим пользователя ввести ID, чье имя хотим узнать
    bot.send_message(message.chat.id, "Введите ID пользователя, чтобы узнать его имя:")

@bot.message_handler(func=lambda message: True)
def handle_user_id(message):
    try:
        # Пытаемся преобразовать текст сообщения в целое число (ID пользователя)
        user_id = int(message.text)

        # Получаем информацию о пользователе по его ID
        user_info = bot.get_chat(user_id)

        # Извлекаем имя пользователя из информации о пользователе
        username = user_info.username

        # Отправляем имя пользователя в чат
        bot.send_message(message.chat.id, f"Имя пользователя с ID {user_id}: {username}")
    except ValueError:
        # Если не удалось преобразовать введенный текст в целое число, то это не является валидным ID
        bot.send_message(message.chat.id, "Ошибка: Введите валидный ID пользователя (целое число).")
    except telebot.TeleBotException as e:
        # Если возникает ошибка, например, пользователь не найден или нельзя отправить сообщение, обрабатываем её
        bot.send_message(message.chat.id, f"Ошибка при получении информации о пользователе: {e}")

# Запустите бота
bot.polling()