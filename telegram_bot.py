import telebot

import config
import transform_frames
# а телега за такое банит
bot = telebot.TeleBot(config.telegram_bot_settings.token[0])


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    for i in range(393, 600):
        braille = transform_frames.get_converted_image(
            f'frames/frame{i}.jpg', width=75)
        frame = ''
        for e in braille:
            frame += ''.join(e)+'\n'
        bot.send_message(message.from_user.id, frame)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
