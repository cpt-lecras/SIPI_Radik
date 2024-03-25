from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.enums import ParseMode


import kb
import text
import utils

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.T_start.format(name=msg.from_user.full_name), reply_markup=kb.mainmenu)


@router.message(F.text=="📄 Инфо")
async def start_handler(msg: Message):
    await msg.answer("инфо")


@router.message(F.text=="⚙️ Профиль")
async def start_handler(msg: Message):
    await msg.answer(text.T_profile.format(name=msg.from_user.full_name, group="NONE"), parse_mode=ParseMode.MARKDOWN_V2,reply_markup=kb.inl_setgroup)
    #Вызов функции с проверкой
    #utils.profile(msg)


@router.callback_query(F.data == "set_group_profile")
async def callback_handler(callback: CallbackQuery ):
    await callback.message.answer("GROUP")
    await callback.answer()



@router.message(F.text=="📊 Другая группа")
async def start_handler(msg: Message):
    await msg.answer("инфо")


@router.message(F.text=="📅 Мое Расписание")
async def start_handler(msg: Message):
    await msg.answer("инфо")


@router.message()
async def start_handler(msg: Message):
    await msg.answer("Не понял -_-")
