from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("ā” Channel ", url="https://t.me/Jimi_Bots")],
		[InlineKeyboardButton("Report Bugs šØ", url="https://t.me/Jimibots_grp")]
                ])

	help_image = "https://telegra.ph/file/1e0a3145c7273f446b000.jpg"
	await message.reply_photo(help_image,  caption="**š” HELP š...**\n \n__ā¢ Just Send your Youtube video url š__ \n__ā¢ And i will give Method list to select your choice š__\n \n======================\n__ā¢ š This bot is fully free.__\n`ā¢ā Don't pay anyone for Bots like this.`\n\nā” ```Bot By @Jimi_Bots``` šØ\n",reply_markup=alpha2)
