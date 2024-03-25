from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

# START keyboard
mainmenu = [
    [KeyboardButton(text="📄 Инфо"),KeyboardButton(text="⚙️ Профиль"),KeyboardButton(text="📊 Другая группа")],
    [KeyboardButton(text="📅 Мое Расписание")]
]
mainmenu = ReplyKeyboardMarkup(keyboard=mainmenu,resize_keyboard=True)


# PROFILE SET Group kb inl
inl_setgroup=[[InlineKeyboardButton(
        text="Установить группу",
        callback_data="set_group_profile")]]
inl_setgroup=InlineKeyboardMarkup(inline_keyboard=inl_setgroup)

# BETA keyboard
menu = [
    [InlineKeyboardButton(text="📝 BUTTON 1", callback_data="func_but1"),
    InlineKeyboardButton(text="🖼 BUTTON 2", callback_data="func_but1")]
    ]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
