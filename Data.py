from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Dor! {}

{} Memudahkan Anda Mengambil String
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
**Kamu tidak percaya dengan bot ini?**
1. *Blokir Bot ini*
2. *Delete Chat.*
*MAU MAKE / ENGGA TERSERAH*
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
**Masih disini?**
*Baiklah Silakan Pencet /generate*
*String Pyrogram untuk Bot Music*
*String Telethon Untuk Userbot*
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
By @Zenzuzu2
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="› Back ‹", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("**» GENERATE STRING «**", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("**» GENERATE STRING «**", callback_data="generate")]
        [
            InlineKeyboardButton("*Butuh bantuan❔*", callback_data="help"),
            InlineKeyboardButton("*About Me❔*", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Info Bot
/help - Butuh Bantuan?
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
💡 **About Zenzu String**

*Bot Untuk Mengambil String Dengan Mudah*
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
👋Owner : [Zenzu](https://t.me/Zenzuzu2)
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
☕Channel : [Black Market](https://t.me/Market_Userbot)
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
💫Groups : [Black Market](https://t.me/markettblack)
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
✨*Thanks for using my bots*✨
    """
