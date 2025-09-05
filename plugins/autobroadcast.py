import asyncio

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import AUTO_GCAST, AUTO_GCAST_MSG, LOG_GROUP_ID
from MOONMUSIC import app
from MOONMUSIC.utils.database import get_served_chats

# Convert AUTO_GCAST to boolean based on "On" or "Off"
AUTO_GCASTS = AUTO_GCAST.strip().lower() == "on"

START_IMG_URLS = "https://envs.sh/ouR.jpg"

MESSAGE = f"""𝐈ᴛ'ꜱ 𝐓ʜᴇ 𝐌ᴏꜱᴛ 𝐓ʜᴇᴍᴇ-ᴀʙʟᴇ 𝐎ꜰ 𝐀ʟʟ 𝐒ᴩᴇᴄɪꜰɪᴄ 𝐁ᴏᴛꜱ 𝐓ʜᴇ 𝐍ᴇᴛᴡᴏʀᴋ 𝐈ꜱ 𝐁ᴀꜱᴇᴅ 𝐎ɴ 𝐃ᴇᴠᴇʟᴏᴩɪɴɢ 𝐁ᴏᴛꜱ 𝐀ɴᴅ 𝐆ɪᴠɪɴɢ 𝐓ʜᴇ 𝐒ᴄᴏᴩᴇ 𝐎ꜰ 𝐀ʟʟ 𝐅ᴇᴀᴛᴜʀᴇꜱ 𝐎ꜰ 𝐓ʜᴇ 𝐔ᴩᴄᴏᴍɪɴɢ 𝐁ᴏᴛꜱ.

𝐅ʀᴏᴍ 𝐓ʜᴇ 𝐍ᴇᴛᴡᴏʀᴋ - 𝐖ᴇ 𝐀ʀᴇ 𝐏ʀᴇꜱᴇɴᴛɪɴɢ 𝐓ʜᴇ 

𝐈ᴛ 𝐈ꜱ 𝐎ɴᴇ 𝐎ꜰ 𝐓ʜᴇ 𝐌ᴏꜱᴛ 𝐀ᴅᴠᴀɴᴄᴇᴅ 𝐁ᴏᴛꜱ 𝐈ɴ 𝐓ʜᴇ 𝐍ᴇᴛᴡᴏʀᴋ.

𝐖ʜɪᴄʜ 𝐇ᴀꜱ 𝐁ᴇᴇɴ 𝐔ᴩᴅᴀᴛᴇᴅ 𝐒ɪɴᴄᴇ 𝐀 𝐖ʜɪʟᴇ.


🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏",
                url=f"https://t.me/MoonXmusics_bot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGE

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴɢ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ.**\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (Off)]**"""


async def send_text_once():
    try:
        await app.send_message(LOG_GROUP_ID, TEXT)
    except Exception as e:
        pass


async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(
                        chat_id,
                        photo=START_IMG_URLS,
                        caption=caption,
                        reply_markup=BUTTON,
                    )
                    await asyncio.sleep(
                        20
                    )  # Sleep for 20 seconds between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats


async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCASTS:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(100000)


# Start the continuous broadcast loop if AUTO_GCASTS is True
if AUTO_GCASTS:
    asyncio.create_task(continuous_broadcast())
