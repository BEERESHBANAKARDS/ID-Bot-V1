from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("📢 CHANNEL 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"t.me/BAGURUJOINAGUUKANNADAMOVIES_17"),
       InlineKeyboardButton("bot", url=f"t.me/BAGURUJOINAGUUKANNADAMOVIES_17")
       ],[
       InlineKeyboardButton("⬇️ 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 ⬇️", callback_data="help")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐝", callback_data="id"),
       InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨", callback_data="info")
       ],[
       InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="start"),
       InlineKeyboardButton("⬇️ 𝐂𝐥𝐨𝐬𝐞", callback_data="close"),
       InlineKeyboardButton("🤠 𝐀𝐛𝐨𝐮𝐭", callback_data="about")
       ]]
       )

ABOUT_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🔙 𝐁𝐚𝐜𝐤", callback_data="help"),
       InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="start"),
       InlineKeyboardButton("⬇️ 𝐂𝐥𝐨𝐬𝐞", callback_data="close")
       ]]
       )
