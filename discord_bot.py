import discord
from discord.ext import commands

import asyncio
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


@bot.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command(pass_context=True)
async def bad_apple(ctx):
    message = await ctx.send(f"Нет блин, добрая груша, но яблоко злое, а злое оно потому что пинг {bot.latency} это довольно много")
    for i in range(3, 0, -1):
        await asyncio.sleep(1)
        await message.edit(content=str(i))
    i = 350
    while i < 6571:
        old_time = time.time()
        frame = transform_frames.get_converted_image(
            f'frames/frame{i}.jpg', width=150)
        await message.edit(content=frame)
        i += int((time.time()-old_time)*30)
    await ctx.send('усё')
if __name__ == "__main__":
    bot.run(token)
