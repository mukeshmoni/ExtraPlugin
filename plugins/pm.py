import re
from pyrogram import filters
import random
from MOONMUSIC import app


@app.on_message(filters.command(["m", "m", "m", "m"], prefixes=["p", "d", "P", "D"]))
async def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        await app.send_sticker(message.chat.id, sticker_id)
        await message.reply_text(
            f"**𝐊ᴀʀᴜᴍᴀ 𝐈ᴠᴀɴ 𝐈ʀᴜᴋᴀ  𝐆ʀᴘ 𝐕ᴀɴᴛʜᴀʟᴇʏʏ 𝐏ᴍ  𝐊ᴜᴘᴅʀᴀ  😐😒</b>\n\n<b> {sender}</b>\n\n<b>𝐀ᴅᴍɪɴ 𝐓ʜᴀ 𝐒ᴏʟʟɪ 𝐁ᴀɴ 𝐏ᴀɴɴɪʀᴜᴠᴇᴀ 𝐎ᴅᴜᴅᴀᴀᴀ 𝐓ʜᴀʀᴋᴜʀɪɪɪ....🤨😏🤧**"
        )
    else:
        emoji = get_random_emoji()
        await app.send_message(message.chat.id, emoji)
        await message.reply_text(
            f"**𝐊ᴀʀᴜᴍᴀ 𝐈ᴠᴀɴ 𝐈ʀᴜᴋᴀ  𝐆ʀᴘ 𝐕ᴀɴᴛʜᴀʟᴇʏʏ 𝐏ᴍ  𝐊ᴜᴘᴅʀᴀ  😐😒</b>\n\n<b> {sender}</b>\n\n<b>𝐀ᴅᴍɪɴ 𝐓ʜᴀ 𝐒ᴏʟʟɪ 𝐁ᴀɴ 𝐏ᴀɴɴɪʀᴜᴠᴇᴀ 𝐎ᴅᴜᴅᴀᴀᴀ 𝐓ʜᴀʀᴋᴜʀɪɪɪ....🤨😏🤧</b>\n\n<b>{emoji}**"
        )


def get_random_sticker():
    stickers = [
        "CAACAgQAAxkBAALZpWY1MUYQmrASes0JpBe70dFGgcpiAAKJDwACMcl5UE7RAAHxK5930jQE", # Sticker 1
        "CAACAgUAAxkBAALZpmY1MUYdYunbrBIQ3DgB9By99i2PAAK2BwACCZ7xVkhoBBIY0oN-NAQ", # Sticker 2
        "CAACAgUAAxkBAALZp2Y1MUZFAqesLX8jSUomX31B6uJXAAKMBwACDoyYVESTFNT7TFV4NAQ", # Sticker 3
        "CAACAgUAAxkBAALZqGY1MUYeiCMAAdMvM80KwRQLxLgZ9QAC8AMAAlmjQFe_-1Nm8KztUjQE", # Sticker 4
        "CAACAgEAAxkBAALZqWY1MUZ70Ixn4qzh5oFOLEgcJQ-5AAKqAwACUSkNOd-LYal39EzYNAQ", # Sticker 5
        "CAACAgUAAxkBAALZqmY1MUbMXhdrMvSaEwkSalUzEcLaAAI3BAACy3pwVhGdCJof5bH3NAQ", # Sticker 6
        "CAACAgQAAxkBAALZuGY1MlinNGHvqSts3RldSHzAbctsAAJ_EgACcCChUzeugqgZ9av1NAQ", # Sticker 7
        "CAACAgUAAxkBAALZuWY1Mpe1jgFa9fgrmLa6rL8h3PV7AAKSBgAC0HxZViT81U9saT7oNAQ", # Sticker 8
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "🤬",
        "😤",
    ]
    return random.choice(emojis)
