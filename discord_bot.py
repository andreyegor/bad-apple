import discord
from discord.ext import commands

import time

import transform_frames
import config
import data

transform_frames.pattern = data.mono_braille_pattern
print(data.mono_braille_pattern[(0, 0, 0, 0, 0, 0)])
# я без понятия как сделать это быстрее
token = config.discord_bot_settings.token[0]

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

bot = commands.Bot(command_prefix='!', intents=intent)


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент


@bot.command(pass_context=True)
async def bad_apple(ctx):
    await ctx.send(f"Нет блин, злая груша, а злая она потому что пинг {bot.latency} это довольно много")
    time.sleep(1)
    i = 350
    while i < 6571:
        old_time = time.time()
        braille = transform_frames.get_converted_image(
            f'frames/frame{i}.jpg', width=150)
        frame = ''
        for e in braille:
            frame += ''.join(e)+'\n'
        await ctx.channel.send(frame)
        i += int((time.time()-old_time)*30)
    await ctx.send('усё')
if __name__ == "__main__":
    bot.run(token)
