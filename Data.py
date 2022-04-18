from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can download profile pictures, videos, images and reels from instagram along with post caption.
You can also authorize me to download private posts.

 learn more Click buttons

By @mylog_channel
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ STATUS 🌺", url="https://t.me/mylog_channel")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About ", callback_data="about")
        ],
        [InlineKeyboardButton("More Amazing bots ♻️", url="https://t.me/mylog_channel")],
    ]

    # Help Message
    HELP = """
1) **Images, Videos and Reels**
Send the link here to get the post contents including caption.

2) **Profile Pictures**
Use the command `/profile_pic` or `/dp` along with instagram username to get its profile picture.
Example : `/dp skedits`

3) **Private Posts**
Authorize the bot to download private posts. Use /auth

**Note** : Stories and IGTV are not supported.

Use /auth to authorize and /unauth to unauthorize.
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to download instagram content by @mylog_channel

Source Code : [Click Here](https://github.com/KilobyteStrean/InstagramBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer

Noob Dev : @sathish3451

    """
