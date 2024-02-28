from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="📝 BUTTON 1", callback_data="func_but1"),
    InlineKeyboardButton(text="🖼 BUTTON 2", callback_data="func_but1")]
    ]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
