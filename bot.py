from time import sleep
import config
import logging
import texts
import re
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

logging.basicConfig(level=logging.INFO)

PORT = int(os.environ.get("PORT", 5000))
TOKEN = os.environ("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    #keyboard = types.ReplyKeyboardMarkup()
    #button_1 = types.KeyboardButton(text="С пюрешкой")
    #keyboard.add(button_1)
    #button_2 = "Без пюрешки"
    #keyboard.add(button_2)
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    services = types.KeyboardButton(texts.services)
    address = types.KeyboardButton(texts.address)
    contacts = types.KeyboardButton(texts.contacts)
    about = types.KeyboardButton(texts.about_me)
    text = f'Привет, <b>{message.from_user.first_name}</b> ☺️\nЯ Чат-Бот Жибек 🤖!'
    keyboard.add(services, address, contacts, about)
    photo = open("kitten3.jpg", "rb")

    await message.answer(text, reply_markup=keyboard, parse_mode="html")
    sleep(0.5)
    await message.answer_photo(photo)
    sleep(0.5)
    await message.answer("Чем я могу тебе помочь?")

@dp.message_handler()
async def echo(message: types.Message):
    if message.text == texts.back:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        services = types.KeyboardButton(texts.services)
        address = types.KeyboardButton(texts.address)
        contacts = types.KeyboardButton(texts.contacts)
        about = types.KeyboardButton(texts.about_me)
        markup.add(services, address, contacts, about)
        photo = open("kitten3.jpg", "rb")
        await message.answer_photo(photo)
        sleep(0.5)
        await message.answer("Чем я могу тебе помочь?", reply_markup=markup)

    elif message.text == texts.services:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        lashes = types.KeyboardButton(texts.lashes)
        brows = types.KeyboardButton(texts.brows)
        markup.add(lashes, brows)
        await message.answer("Выберите вид услуг:", reply_markup=markup)

    elif message.text == texts.brows:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(texts.pm_main)
        corr = types.KeyboardButton(texts.pm_corr)
        rem = types.KeyboardButton(texts.remove_pm)
        notice = types.KeyboardButton(texts.notice)
        markup.add(main, corr, rem, notice)
        await message.answer("Перманентный макияж бровей.\nВиды услуг:", reply_markup=markup)

    elif message.text == texts.lashes:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer("Наращивание ресниц.\nВиды услуг:", reply_markup=markup)

    elif message.text == texts.contacts:
        markup = types.InlineKeyboardMarkup(row_width=1)
        instagram = types.InlineKeyboardButton("Мой Instagram 📸", url="https://instagram.com/browbarmsk")
        whatsapp = types.InlineKeyboardButton("Мой WhatsApp 📱", url="https://wa.me/79999788423")
        telegram = types.InlineKeyboardButton("Мой Telegram 📲", url="https://t.me/dokbaeva")
        markup.add(instagram, whatsapp, telegram)
        await message.answer(texts.CONTACTS, reply_markup=markup)

    elif message.text == texts.address:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Маршрут 🗺", "https://go.2gis.com/08fgl"))
        await message.answer(texts.ADDRESS, reply_markup=markup)

    elif message.text == texts.about_me:
        await message.answer(texts.ABOUT_ME)

    elif message.text == texts.extra:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer("Дополнительные услуги:", reply_markup=markup)

    elif message.text == texts.pm_main:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(texts.services)
        corr = types.KeyboardButton(texts.pm_corr)
        rem = types.KeyboardButton(texts.remove_pm)
        notice = types.KeyboardButton(texts.notice)
        markup.add(main, corr, rem, notice)
        await message.answer(texts.PM_MAIN, reply_markup=markup)

    elif message.text == texts.pm_corr:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(texts.pm_main)
        corr = types.KeyboardButton(texts.services)
        rem = types.KeyboardButton(texts.remove_pm)
        notice = types.KeyboardButton(texts.notice)
        markup.add(main, corr, rem, notice)
        await message.answer(texts.PM_CORR, reply_markup=markup)

    elif message.text == texts.remove_pm:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(texts.pm_main)
        corr = types.KeyboardButton(texts.pm_corr)
        rem = types.KeyboardButton(texts.services)
        notice = types.KeyboardButton(texts.notice)
        markup.add(main, corr, rem, notice)
        await message.answer(texts.REMOVE_PM, reply_markup=markup)

    elif message.text == texts.notice:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(texts.pm_main)
        corr = types.KeyboardButton(texts.pm_corr)
        rem = types.KeyboardButton(texts.remove_pm)
        notice = types.KeyboardButton(texts.services)
        markup.add(main, corr, rem, notice)
        await message.answer(texts.NOTICE,reply_markup=markup)
    
    elif message.text == texts.classic:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.services)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(texts.CLASSIC, reply_markup=markup)

    elif message.text == texts.one_five:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.services)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(texts.ONE_FIVE, reply_markup=markup)

    elif message.text == texts.two:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.services)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(texts.TWO, reply_markup=markup)

    elif message.text == texts.two_five:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.services)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(texts.TWO_FIVE, reply_markup=markup)

    elif message.text == texts.three:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.services)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(texts.THREE, reply_markup=markup)

    elif message.text == texts.hollywood:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.services)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        await message.answer(texts.HOLLYWOOD, reply_markup=markup)

    elif message.text == texts.curve_l:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.back)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(texts.CURVE_L, reply_markup=markup)

    elif message.text == texts.curve_m:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.back)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(texts.CURVE_M, reply_markup=markup)

    elif message.text == texts.spec_wide:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.back)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(texts.SPEC_WIDE, reply_markup=markup)

    elif message.text == texts.fixer:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.back)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(texts.FIXER, reply_markup=markup)

    elif message.text == texts.kylie_effect:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.back)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(texts.KYLIE_EFFECT, reply_markup=markup)

    elif message.text == texts.remove_lashes:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.back)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        await message.answer(texts.REMOVE_LASHES, reply_markup=markup)

    else:
        markup = types.InlineKeyboardMarkup(row_width=1)
        instagram = types.InlineKeyboardButton("Мой Instagram 📸", "https://instagram.com/browbarmsk")
        whatsapp = types.InlineKeyboardButton("Мой WhatsApp", url="https://wa.me/79999788423")
        telegram = types.InlineKeyboardButton("Мой Telegram", url="https://t.me/dokbaeva")
        markup.add(instagram, whatsapp, telegram)
        await message.answer("Я не знаю что ты имеешь ввиду🥺\nНо ты можешь написать мне ⬇️", reply_markup=markup)


    
    #await bot.send_message(message.chat.id, message.text)
    #await message.answer(message.text.upper())



#@dp.message_handler(Text(equals="С пюрешкой"))
#async def with_puree(message: types.Message):
#    await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())
#
#@dp.message_handler(lambda message: message.text == "Без пюрешки")
#async def without_puree(message: types.Message):
#    await message.reply("Так невкусно!", reply_markup=types.ReplyKeyboardRemove())

#@dp.message_handler(commands='starts')
#async def send_welcome(message: types.Message):
 #   """
  #  This handler will be called when user sends `/start` or `/help` command
#    """
   # await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
#    buttons = [
#        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
#        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram"),
#    ]
#    keyboard = types.InlineKeyboardMarkup(row_width=1)
#    keyboard.add(*buttons)
#    await message.answer("Hi Friend! How can I help you?", reply_markup=keyboard)
#
#@dp.message_handler(commands="starts")
#async def cmd_start(message: types.Message):
#    keyboard = types.ReplyKeyboardMarkup()
#    button_1 = types.KeyboardButton(text="С пюрешкой")
#    keyboard.add(button_1)
#    button_2 = "Без пюрешки"
#    keyboard.add(button_2)
#    await message.answer("Как подавать котлеты?", reply_markup=keyboard)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)