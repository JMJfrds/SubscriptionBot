from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

check = InlineKeyboardMarkup(inline_keyboard=[

    [InlineKeyboardButton(text="Kanal nomi", url="")],
    [InlineKeyboardButton(text="Tekshirish", callback_data="_check_")],
])