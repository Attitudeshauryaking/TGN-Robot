import os
from pyrogram import Client, filters
from pyrogram.types import *

from TGNRobot.conf import get_str_key
from TGNRobot import pbot

REPO_TEXT = "**🔥A Powerful [BOT](https://telegra.ph/file/9560aa796165f09b35165.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [ཧᜰ꙰ꦿ➢𝐎𝐀𝐍༒](t.me/ItsAttitudeking) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @Attitude_Network «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("🛠️ʀᴇᴘᴏꜱɪᴛᴏʀʏ🛠️", url=f"https://github.com/ItsAttitudeking")
      ],[
        InlineKeyboardButton("➢𝐎𝐀𝐍 ☛ ᴏᴡɴᴇʀ", url="https://t.me/ItsAttitudeking"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/OAN_Support"),
      ],[
        InlineKeyboardButton("⚡ᴜᴘᴅᴀᴛᴇꜱ☑️", url="https://t.me/Attitude_Network")
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
