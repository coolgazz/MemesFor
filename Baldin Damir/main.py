import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6176406686:AAF0lrRVkh6V3uoc9_FUz1gvX-DRloP2qeQ'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['hi', 'pomogi'])
async def send_welcome(message: types.Message):
    await message.reply("Privet!\nYa EchoBot Damira\nRabotayu na aiogram.")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here 😺')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)