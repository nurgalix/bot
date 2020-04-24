# coding=utf-8
import telebot
import config

bot = telebot.TeleBot(config.token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Почему?', 'Пока')


# bot.send_message(771034229, '')  # Что бы отправить себе сообщения, первый аргумент id второй текст
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет создатель!', reply_markup=keyboard1)
    # print(message)  # информация


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'почему?':
        bot.send_message(message.chat.id, 'Потому что он меня создал.')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    else:
        bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)


if __name__ == '__main__':
    bot.infinity_polling()
