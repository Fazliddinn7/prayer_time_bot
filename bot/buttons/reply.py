
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

from bot.buttons.text import subscribe_text


def subscribeKeyboard():
    keyboard = KeyboardButton(text=subscribe_text)
    design = [
        [keyboard]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


def regions_keyboard():
    b1 = KeyboardButton(text='Toshkent')
    b2 = KeyboardButton(text='Fargana')
    b3 = KeyboardButton(text='Andijon')
    b4 = KeyboardButton(text='Buxoro')
    b5 = KeyboardButton(text='Guliston')
    b6 = KeyboardButton(text='Samarqand')
    b7 = KeyboardButton(text='Namangan')
    b8 = KeyboardButton(text='Navoiy')
    b9 = KeyboardButton(text='Jizzax')
    b10 = KeyboardButton(text='Nukus')
    b11 = KeyboardButton(text='Qarshi')
    b12 = KeyboardButton(text='Xiva')
    b13 = KeyboardButton(text='Qoqan')


    design = [
        [b1, b2, b3],
        [b4, b5, b6],
        [b7, b8, b9],
        [b10, b11, b12],
        [b13]
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
    return rkm


def unsubscribe_keyboard():
    b1 = KeyboardButton(text='❌ Obunani to\'xtatish')
    b2 = KeyboardButton(text='☪️ Bugungi namoz vaqtlari')
    design = [
        [b1],
        [b2]
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
    return rkm
