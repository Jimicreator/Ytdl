from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("⚡ Channel ", url="https://t.me/Jimi_Bots")],
		[InlineKeyboardButton("Report Bugs 🚨", url="https://t.me/Jimibots_grp")]
                ])

	help_image = "https://telegra.ph/file/1e0a3145c7273f446b000.jpg"
	await message.reply_photo(help_image,  caption="**💡 HELP 📃...**\n \n__• Just Send your Youtube video url 🌟__ \n__• And i will give Method list to select your choice 😋__\n \n======================\n__• 😊 This bot is fully free.__\n`•⚙ Don't pay anyone for Bots like this.`\n\n⚡ ```Bot By @Jimi_Bots``` 🚨\n",reply_markup=alpha2)
