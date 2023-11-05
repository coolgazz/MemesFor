from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token="6926824789:AAE4DNh1vFQmYdrz_glNJ8YmnDuU5WoatCM")
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Ну здарова!")

@dp.message_handler(lambda message: message.text.lower() in ["перестань", "хватит", "прекрати"])
async def stop_bot(message: types.Message):
    await message.reply("Нет!")

@dp.message_handler(lambda message: message.text.lower() == "как тебя выключить?")
async def turn_off_bot(message: types.Message):
    await message.reply("Я сам тебя выключу !")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
