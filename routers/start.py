from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards import check
from config import CHANNEL
from main import bot

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"<b>Assalomu Aleykum {message.from_user.mention_html()}!</b>",
                        reply_markup=check)


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Sizga qanday yordam bera olaman ?")


@router.callback_query(F.data == '_check_')
async def cmd_check(call: types.CallbackQuery):
    user_status = await bot.get_chat_member(CHANNEL, call.from_user.id)
    if user_status.status == "left":
        await call.answer("Kanalga xali obuna bo'lmagansiz !\nBirinchi kanalga obuna bo'ling", show_alert=True)
        await call.message.answer("<b>Botdan foydalanish uchun birinchi kanalga obuna bo'ling</b>", reply_markup=check)
        return

    await call.answer("<b>Botdan foydalanishingiz mumkin ✅</b>")