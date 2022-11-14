import telebot

import config
import transform_frames
import data

from time import sleep, time
import func_timeout
# а телега за такое банит
bots = list(map(telebot.TeleBot, config.telegram_bot_settings.tokens))
big_bot = bots[0]
transform_frames.pattern = data.mono_braille_pattern


@big_bot.message_handler(content_types=['text'])
def get_text_messages(message):
    i = 1
    messages = {}
    # for bot in bots:
    #     messages[bot] = bot.send_message(message.from_user.id, '😐🔫')
    tm = time()
    frame = '😐🔫'
    while i < 6571:
        for bot in bots:
            i_old = i
            that_message = bot.send_message(message.chat.id, frame)
            print(time()-tm)
            while i < i_old+150:
                i += int((time()-tm)*60)
                tm = time()
                frame = transform_frames.get_converted_image(
                    f'frames/frame{i}.jpg', width=55)
                tm = time()
                try:

                    if that_message.text[:-5] != frame:

                        func_timeout.func_timeout(0.5, bot.edit_message_text, kwargs={
                            'chat_id': that_message.chat.id, 'message_id': that_message.message_id, 'text': frame+f'{i:05}'})
                        print(time()-tm)

                except func_timeout.FunctionTimedOut:
                    break


if __name__ == '__main__':
    big_bot.polling(none_stop=True, interval=0)
