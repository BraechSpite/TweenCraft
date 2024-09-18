from flask import Flask
from threading import Thread
import os
from telethon import TelegramClient, events, Button
app = Flask(__name__)
@app.route('/')
def index():
    return 'Server is running!'
def run_flask():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# API credentials
api_id = 23909122
api_hash = 'b4f075a6f01edb569f25fb5a4183d383'
bot_token = '7483575611:AAH6Xbejtx1Qtqko-2TK58UEzXewMHCwmy8'

# Create the bot client
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Define the start command handler
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await send_main_menu(event)

async def send_main_menu(event):
    try:
        # Get the user's first name and create a link to their profile
        user = await bot.get_entity(event.sender_id)
        user_link = f"{user.first_name}"
    except Exception as e:
        user_link = "User"
        print(f"Failed to fetch user details: {e}")
    
    # Define the welcome message
    welcome_message = f"""
✨ 𝙃𝙚𝙡𝙡𝙤 👋🏻 {user_link} 𝙒𝙚𝙡𝙘𝙤𝙢𝙚 ✨

🎉  𝙒𝙚 𝙋𝙧𝙤𝙫𝙞𝙙𝙚 𝙔𝙤𝙪 𝙏𝙬𝙚𝙚𝙣𝘾𝙧𝙖𝙛𝙩 𝙈𝙤𝙙 𝙏𝙝𝙖𝙩 𝙒𝙤𝙧𝙠𝙨 𝙋𝙚𝙧𝙛𝙚𝙘𝙩𝙡𝙮 𝙁𝙞𝙣𝙚, 𝙏𝙝𝙖𝙩 𝙃𝙖𝙨 𝘼𝙡𝙡 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 𝙁𝙚𝙖𝙩𝙪𝙧𝙚𝙨 𝙐𝙣𝙡𝙤𝙘𝙠𝙚𝙙 𝘼𝙣𝙙 𝙔𝙤𝙪 𝘾𝙖𝙣 𝙐𝙨𝙚 𝙏𝙝𝙚𝙢 𝙒𝙞𝙩𝙝𝙤𝙪𝙩 𝘼𝙣𝙮 𝙄𝙨𝙨𝙪𝙚𝙨.
➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖
👏🏻 𝘽𝙪𝙩 𝙎𝙞𝙣𝙘𝙚 𝙒𝙚 𝙆𝙚𝙚𝙥 𝙐𝙥𝙙𝙖𝙩𝙞𝙣𝙜 𝙏𝙝𝙚 𝘼𝙥𝙥 𝘼𝙣𝙙 𝙄𝙩 𝘾𝙤𝙨𝙩𝙨 𝙏𝙤𝙤 𝙈𝙪𝙘𝙝 𝙏𝙤𝙤 𝙐𝙨 𝘽𝙪𝙩 𝙒𝙚 𝙎𝙩𝙞𝙡𝙡 𝙋𝙧𝙤𝙫𝙞𝙙𝙚 𝙄𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪 𝙂𝙪𝙮𝙨, 𝙎𝙤 𝙒𝙚 𝘾𝙝𝙖𝙧𝙜𝙚 𝙁𝙤𝙧 𝙏𝙝𝙚 𝙈𝙤𝙙 𝘼𝙣𝙙 𝙄𝙩'𝙎 𝙋𝙧𝙞𝙘𝙚 𝙄𝙎 𝙍𝙚𝙖𝙨𝙤𝙣𝙖𝙗𝙡𝙚 𝘼𝙣𝙙 𝘾𝙝𝙚𝙖𝙥 𝙅𝙪𝙨𝙩 100₹ | 1.5$ 
➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖
➡️ TO GET ᗰOᗪ ᑕᒪIᑕK Oᑎ GET ᗰOᗪ 
➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖
🎥 GET ᐯIᗪEO TᑌTOᖇIᗩᒪ Oᑎ ᕼOᗯ TO GET ᗰOᗪ 
➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖
🧾𝗣𝗥𝗢𝗢𝗙𝗦🧾
➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖
💬 𝗬𝗼𝘂 𝗖𝗮𝗻 𝗦𝗲𝗻𝗱 𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗔𝗹𝘀𝗼 𝗜 𝗪𝗶𝗹𝗹 𝗥𝗲𝗽𝗹𝘆 𝗧𝗼 𝗧𝗵𝗲𝗺 

🤝 𝙏𝙝𝙖𝙣𝙠𝙨 🤝
    """
    
    # Create inline buttons side by side
    buttons = [
        [Button.inline("✨ GET MOD ✨", b"get_mod")],
        [Button.inline("🎥 GET VIDEO TUTORIAL 🎥", b"get_tutorial")],
        [Button.url("🧾𝗣𝗥𝗢𝗢𝗙𝗦🧾", url="https://www.tumblr.com/thereapersmokes/761943793308139520/proofs-for-tweencraft-mod?source=share")],
        [Button.inline("🔘 𝗕𝗔𝗖𝗞 𝗧𝗢 𝗠𝗘𝗡𝗨𝗘 🔘", b"back_to_menu")]
    ]
    
    # Send the message with buttons
    await event.respond(welcome_message, buttons=buttons, link_preview=False)

# Handle button presses
@bot.on(events.CallbackQuery)
async def callback(event):
    if event.data == b"get_mod":
        # Define the message with the new inline button
        mod_message = """
𝗦𝗧𝗘𝗣𝗦 𝗧𝗢 𝗚𝗘𝗧 𝗧𝗪𝗘𝗘𝗡𝗖𝗥𝗔𝗙𝗧 𝗠𝗢𝗗

1️⃣ 👉🏻 𝗖𝗟𝗜𝗖𝗞 𝗢𝗡 𝗚𝗥𝗔𝗕 𝗠𝗢𝗗
 
2️⃣ 👉🏻 𝗦𝗘𝗟𝗘𝗖𝗧 𝗣𝗔𝗬𝗠𝗘𝗡𝗧 𝗠𝗘𝗧𝗛𝗢𝗗 𝗜𝗙 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗜𝗡𝗗𝗜𝗔𝗡 𝗖𝗟𝗜𝗖𝗞 𝗢𝗡 💰 𝗨𝗣𝗜/𝗚𝗣𝗔𝗬/𝗣𝗛𝗢𝗡𝗘 𝗣𝗔𝗬 💰

3️⃣ 👉🏻 𝗜𝗙 𝗬𝗢𝗨 𝗔𝗥𝗘 𝗙𝗥𝗢𝗠 𝗢𝗧𝗛𝗘𝗥 𝗖𝗢𝗨𝗡𝗧𝗥𝗜𝗘𝗦 𝗨𝗦𝗘 𝗕𝗜𝗡𝗔𝗡𝗖𝗘 𝗣𝗔𝗬 [ 𝗔 𝗖𝗥𝗬𝗣𝗧𝗢 𝗪𝗔𝗟𝗟𝗘𝗧 ] | 𝗖𝗟𝗜𝗖𝗞 𝗢𝗡 𝗕𝗜𝗡𝗔𝗡𝗖𝗘 𝗣𝗔𝗬 |

4️⃣ 👉🏻 𝗦𝗘𝗡𝗗 100₹ | 2$ 𝗧𝗢 𝗧𝗛𝗘 𝗣𝗥𝗢𝗩𝗜𝗗𝗘𝗗 𝗣𝗔𝗬𝗠𝗘𝗡𝗧 𝗜𝗡𝗙𝗢

5️⃣ 👉🏻𝗔𝗙𝗧𝗘𝗥 𝗣𝗔𝗬𝗠𝗘𝗡𝗧 𝗦𝗘𝗡𝗗 𝗔 𝗖𝗟𝗘𝗔𝗥 𝗦𝗖𝗥𝗘𝗘𝗡𝗦𝗛𝗢𝗧 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗪𝗜𝗟𝗟 𝗔𝗨𝗧𝗢𝗠𝗔𝗧𝗜𝗖𝗔𝗟𝗟𝗬 𝗖𝗢𝗡𝗙𝗜𝗥𝗠 𝗧𝗛𝗘 𝗣𝗔𝗬𝗠𝗘𝗡𝗧 𝗔𝗡𝗗 𝗪𝗜𝗟𝗟 𝗚𝗜𝗩𝗘 𝗬𝗢𝗨 𝗧𝗛𝗘 𝗠𝗢𝗗 𝗙𝗜𝗟𝗘

🤝 𝗧𝗛𝗔𝗡𝗞𝗦 🤝
        """
        buttons = [
            [Button.inline("🎁 𝗚𝗥𝗔𝗕 𝗠𝗢𝗗 🎁", b"grab_mod")],
            [Button.inline("🔘 𝗕𝗔𝗖𝗞 𝗧𝗢 𝗠𝗘𝗡𝗨𝗘 🔘", b"back_to_menu")]
        ]
        await event.respond(mod_message, buttons=buttons, link_preview=False)
    elif event.data == b"get_tutorial":
        await event.answer("Video tutorial is coming soon!")
    elif event.data == b"grab_mod":
        buttons = [
            [Button.inline("💰 𝗨𝗣𝗜 | 𝗚-𝗣𝗔𝗬 | 𝗣𝗛𝗢𝗡𝗘 𝗣𝗔𝗬 💰", b"upi_payment")],
            [Button.inline("💰𝗕𝗜𝗡𝗔𝗡𝗖𝗘 𝗣𝗔𝗬 💰", b"binance_payment")],
            [Button.inline("🔘 𝗕𝗔𝗖𝗞 𝗧𝗢 𝗠𝗘𝗡𝗨𝗘 🔘", b"back_to_menu")]
        ]
        await event.respond("Please select your payment method:", buttons=buttons, link_preview=False)
    elif event.data == b"upi_payment":
        qr_caption = """
💳 𝗦𝗖𝗔𝗡 𝗧𝗛𝗜𝗦 𝗤𝗥 𝗔𝗡𝗗 𝗣𝗔𝗬 100₹ 𝗢𝗡 𝗧𝗛𝗜𝗦 | 𝗢𝗡𝗖𝗘 𝗣𝗔𝗜𝗗 𝗦𝗘𝗡𝗗 𝗔 𝗖𝗟𝗘𝗔𝗥 𝗦𝗖𝗥𝗘𝗘𝗡𝗦𝗛𝗢𝗧

🪪 𝗬𝗢𝗨 𝗖𝗔𝗡 𝗔𝗟𝗦𝗢 𝗣𝗔𝗬 𝗢𝗡 𝗧𝗛𝗜𝗦 𝗨𝗣𝗜 𝗜𝗗: `tonyreaper121@okicici` | 𝗢𝗡𝗖𝗘 𝗣𝗔𝗜𝗗 𝗦𝗘𝗡𝗗 𝗔 𝗖𝗟𝗘𝗔𝗥 𝗦𝗖𝗥𝗘𝗘𝗡𝗦𝗛𝗢𝗧

🎉 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗪𝗜𝗟𝗟 𝗔𝗨𝗧𝗢𝗠𝗔𝗧𝗜𝗖𝗔𝗟𝗟𝗬 𝗖𝗢𝗡𝗙𝗜𝗥𝗠 𝗧𝗛𝗘 𝗣𝗔𝗬𝗠𝗘𝗡𝗧 𝗔𝗡𝗗 𝗪𝗜𝗟𝗟 𝗚𝗜𝗩𝗘 𝗬𝗢𝗨 𝗧𝗛𝗘 𝗠𝗢𝗗 𝗙𝗜𝗟𝗘

👏🏻 𝗧𝗛𝗔𝗡𝗞𝗦 👏🏻
        """
        await bot.send_file(event.chat_id, 'My_Qr.png', caption=qr_caption, buttons=[Button.inline("🔘 𝗕𝗔𝗖𝗞 𝗧𝗢 𝗠𝗘𝗡𝗨𝗘 🔘", b"back_to_menu")])
    elif event.data == b"binance_payment":
        qr_caption = """
💳 𝗦𝗖𝗔𝗡 𝗧𝗛𝗜𝗦 𝗤𝗥 𝗧𝗢 𝗣𝗔𝗬 2$ | 𝗢𝗡𝗖𝗘 𝗣𝗔𝗜𝗗 𝗦𝗘𝗡𝗗 𝗔 𝗖𝗟𝗘𝗔𝗥 𝗦𝗖𝗥𝗘𝗘𝗡𝗦𝗛𝗢𝗧

🪪 𝗠𝗬 𝗕𝗜𝗡𝗔𝗡𝗖𝗘 𝗜𝗗: `906981217` 𝗖𝗢𝗣𝗬 𝗜𝗧 𝗔𝗡𝗗 𝗦𝗘𝗡𝗗 2$ 𝗨𝗦𝗜𝗡𝗚 𝗕𝗜𝗡𝗔𝗡𝗖𝗘 | 𝗢𝗡𝗖𝗘 𝗣𝗔𝗜𝗗 𝗦𝗘𝗡𝗗 𝗔 𝗖𝗟𝗘𝗔𝗥 𝗦𝗖𝗥𝗘𝗘𝗡𝗦𝗛𝗢𝗧

🎉 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗪𝗜𝗟𝗟 𝗔𝗨𝗧𝗢𝗠𝗔𝗧𝗜𝗖𝗔𝗟𝗟𝗬 𝗖𝗢𝗡𝗙𝗜𝗥𝗠 𝗧𝗛𝗘 𝗣𝗔𝗬𝗠𝗘𝗡𝗧 𝗔𝗡𝗗 𝗪𝗜𝗟𝗟 𝗚𝗜𝗩𝗘 𝗬𝗢𝗨 𝗧𝗛𝗘 𝗠𝗢𝗗 𝗙𝗜𝗟𝗘

👏🏻 𝗧𝗛𝗔𝗡𝗞𝗦 👏🏻
        """
        await bot.send_file(event.chat_id, 'BI_Qr.png', caption=qr_caption, buttons=[Button.inline("🔘 𝗕𝗔𝗖𝗞 𝗧𝗢 𝗠𝗘𝗡𝗨𝗘 🔘", b"back_to_menu")])
    elif event.data == b"back_to_menu":
        await send_main_menu(event)

# Start the bot
bot.start()
bot.run_until_disconnected()
if __name__ == '__main__':
    run_flask()
