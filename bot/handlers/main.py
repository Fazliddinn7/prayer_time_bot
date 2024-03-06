from datetime import date
from aiogram.types import Message

from bot.buttons.reply import *
from bot.buttons.text import *
from dispatcher import dp
from test import get_prayer_time
subscribe_region = None


@dp.message(lambda msg: msg.text == subscribe_text)
async def handler(message: Message):

    await message.answer("Hududni tanlang 👇🏻", reply_markup=regions_keyboard())


@dp.message(lambda msg: msg.text in [toshkent_txt,quqon_txt,andijon_txt,buxoro_txt,guliston_txt,samarqand_txt,namangan_txt,navoiy_txt,jizzah_txt,nukus_txt,qarshi_txt,xiva_txt, fargona_txt])
async def region_handler(message: Message):
    global subscribe_region
    subscribe_region = message.text
    times = await get_prayer_time(message.text)
    text = f"""
    Bugun {date.today()}.

☪️ Namoz vaqtlari:

Bomdod: {times[0]}
Quyosh: {times[1]}
Peshin: {times[2]}
Asr: {times[3]}
Shom: {times[4]}
Xufton: {times[5]}

Manba: namozvaqti.uz

📢@namoz_toshkent1
📢@namoz_vaqtlari_4
🤖@namaz_vaqti_bot
"""
    await message.answer(text)
    await message.answer("Botga obunani to'xtatish uchun 'Obunani to'xtatish' ga bosing!", reply_markup=unsubscribe_keyboard())


@dp.message(lambda msg: msg.text == '❌ Obunani to\'xtatish')
async def region_handler(msg: Message):
    await msg.answer("Bot sizga namoz vaqlarini jo'natish uchun 'Obuna bo\'lish' tugmasini bosing", reply_markup=subscribeKeyboard())


@dp.message(lambda msg: msg.text == '☪️ Bugungi namoz vaqtlari')
async def region_handler(msg: Message):
    times = await get_prayer_time(subscribe_region)
    text = f"""
            Bugun {date.today()}.

☪️ Namoz vaqtlari:

Bomdod: {times[0]}
Quyosh: {times[1]}
Peshin: {times[2]}
Asr: {times[3]}
Shom: {times[4]}
Xufton: {times[5]}

Manba: namozvaqti.uz

📢@namoz_toshkent1
📢@namoz_vaqtlari_4
🤖@namaz_vaqti_bot"""

    await msg.answer(text)