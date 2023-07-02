from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀𝐝𝐝 𝐖𝐲𝐧𝐤 𝐌𝐮𝐬𝐢𝐜",
                url=f"https://t.me/Wynk_Music_TetrisBot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐇𝐞𝐥𝐩",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀𝐝𝐝 𝐖𝐲𝐧𝐤 𝐌𝐮𝐬𝐢𝐜",
                url=f"https://t.me/Wynk_Music_TetrisBot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐇𝐞𝐥𝐩", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="𝐖𝐲𝐧𝐤", url=f"https://wynk.in/music"
            )
        ],
     ]
    return buttons

