from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from bot.buttons.reply import subscribeKeyboard
from dispatcher import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    text = """
    Assalomu aleykum. Namoz vaqtlari botga xush kelibsiz. Ushbu bot yordamida hohlagan viloyatdagi namoz vaqtlarini bilib olishingiz mumkin.

Barcha ma'lumotlar islom.uz saytidan olinadi!."""
    await message.answer(text)
    await message.answer("Bot sizga namoz vaqtlarini yuborish uchun 'Obuna bo\'lish' tugmasini bosing!",
                         reply_markup=subscribeKeyboard())