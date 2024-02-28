from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


import kb
import text


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.mes_start.format(name=msg.from_user.full_name), reply_markup=kb.menu)


@router.message()
async def start_handler(msg: Message):
    await msg.answer("Не понял -_-")