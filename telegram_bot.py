import telebot

import config
import transform_frames
import data

from time import sleep, time
# а телега за такое банит
bot = telebot.TeleBot(config.telegram_bot_settings.token[0])
transform_frames.pattern = data.mono_braille_pattern


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    that_message = bot.send_message(
        message.from_user.id, '😐🔫')
    old_frame = ''
    for i in range(1, 6571, 30):
        braille = transform_frames.get_converted_image(
            f'frames/frame{i}.jpg', width=55)
        frame = ''
        for e in braille:
            frame += ''.join(e)+'\n'
        if old_frame != frame:
            bot.edit_message_text(chat_id=that_message.chat.id,
                                  message_id=that_message.message_id, text=frame+str(i))
            old_frame = frame
        sleep(1)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
