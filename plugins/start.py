from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Alpha = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("š¤ Jimi Bots š", url="https://t.me/Jimi_Bots")],
        [InlineKeyboardButton("š support š", url="https://t.me/jimibots_grp")]

    ])
    thumbnail_url = "https://telegra.ph/file/1e0a3145c7273f446b000.jpg"
    await message.reply_photo(thumbnail_url, caption=f"**š Hi <b>{message.from_user.first_name}**</b>\n\n<br>__š I Can Download YT Files For You āØļø__</br>\n\n<b>ā¢ **šļø Instructions for use...šØ**</b>\nā¢ **ā Type /help to get instructins...**\n \nāāāāā ā **Lets Play** ā āāāāā\n ", reply_markup=Alpha)
    raise StopPropagation
