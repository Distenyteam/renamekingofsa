
from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	await message.reply_text("Bot :- @renameer2bot\nCreater :- @PiratesDeveloper\nLanguage :-Python3\nLibrary :- Pyrogram 1.4.16\nServer :- Heroku")
	
	
		
@Client.on_message(filters.private & filters.command(["clone"]))
async def start(client,message):
	await message.reply_text(">━━━━━━━━━᚜ PRIVATE BOT ᚛━━━━━━━━━<\nHi, Guys I'am a Developer, If You Need A Bot Like This => PM ME @PiratesDeveloper I Will Also Develope Bot Like Mallu_Movies/ProSearch bot and We Will Also Develope Bot As Your Wish😇\n>━━━━━━━━━᚜ PRIVATE BOT ᚛━━━━━━━━━<")
