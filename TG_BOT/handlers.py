from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import kb
import text
from TG_BOT import db
import states as st

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    """
    start handler
    :param: msg
    :return:
    """
    await msg.answer(text.T_start.format(name=msg.from_user.full_name), reply_markup=kb.mainmenu)
    await db.registrate(msg.from_user.id, msg.from_user.username)


@router.message(F.text=="📄 Инфо")
async def start_handler(msg: Message):
    """
    btn Info handler
    :param msg:
    :return:
    """
    await msg.answer(text.T_info, parse_mode=ParseMode.MARKDOWN_V2)


@router.message(F.text=="⚙️ Профиль")
async def start_handler(msg: Message):
    """
    btn Profile handler
    :param msg:
    :return:
    """
    id=msg.from_user.id
    if (await db.get_group(id)==None):
        await msg.answer(text.T_profile.format(name=msg.from_user.full_name, group="Не установлена"), parse_mode=ParseMode.MARKDOWN_V2, reply_markup=kb.inl_setgroup)
    else:
        await msg.answer(text.T_profile.format(name=msg.from_user.full_name, group=await db.get_group(id)),
                         parse_mode=ParseMode.MARKDOWN_V2, reply_markup=kb.inl_setgroup)




@router.callback_query(F.data == "set_group_profile")
async def callback_handler(callback: CallbackQuery, state: FSMContext):
    """
    callback handler for group setting
    :param callback:
    :param state:
    :return:
    """
    await callback.message.answer("Введи название группы")
    await callback.answer()
    await state.set_state(st.SetGroup.start_write_group)

# STATE 1
@router.message(st.SetGroup.start_write_group)
async def set_group_start(msg: Message, state: FSMContext):
    await state.update_data(group=msg.text.lower())
    #добавить проверку что группа есть в бд
    id = msg.from_user.id
    user_data = await state.get_data()
    await db.set_group(id, user_data['group'])
    await state.clear()
    await msg.answer("Успешно")


@router.message(F.text=="📊 Другая группа")
async def start_handler(msg: Message):
    """
    btn Other group
    :param msg:
    :return:
    """
    await msg.answer("What")


@router.message(F.text=="📅 Мое Расписание")
async def start_handler(msg: Message):
    """
    btn Schedule
    :param msg:
    :return:
    """
    await msg.answer("инфо")


@router.message()
async def start_handler(msg: Message):
    """
    Dont understand message
    :param msg:
    :return:
    """
    await msg.answer("Не понял -_-")
