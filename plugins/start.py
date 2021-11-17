from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Alpha = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("🤓 Jimi Bots 🔎", url="https://t.me/Jimi_Bots")],
        [InlineKeyboardButton("😎 support 🔎", url="https://t.me/jimibots_grp")]

    ])
    thumbnail_url = "https://telegra.ph/file/1e0a3145c7273f446b000.jpg"
    await message.reply_photo(thumbnail_url, caption=f"**🙂 Hi <b>{message.from_user.first_name}**</b>\n\n<br>__😇 I Can Download YT Files For You ✨️__</br>\n\n<b>• **🗂️ Instructions for use...🚨**</b>\n• **⚙ Type /help to get instructins...**\n \n───── ❝ **Lets Play** ❞ ─────\n ", reply_markup=Alpha)
    raise StopPropagation
