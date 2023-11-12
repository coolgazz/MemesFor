from aiogram import Bot, Dispatcher, types, executor
import wikipedia

bot = Bot(token="6939860030:AAGifeA5ybu7iRiokwOtrJL3eWlx7O1W3SA")
dp = Dispatcher(bot)
wikipedia.set_lang("ru")  # Set the language for Wikipedia search

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Включить эхо", callback_data="echo_on"))
    keyboard.add(types.InlineKeyboardButton(text="Включить Википедию", callback_data="wiki_on"))
    await message.answer("Привет! Я твой новый телеграм-бот на aiogram. Выберите функцию:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'echo_on')
async def echo_on(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Эхо включено")

@dp.callback_query_handler(lambda c: c.data == 'wiki_on')
async def wiki_on(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Википедия включена")

@dp.message_handler(lambda message: message.text.startswith('найди'))
async def wiki_search(message: types.Message):
    query = message.text.replace('найди ', '', 1)
    try:
        search_result = wikipedia.summary(query, sentences=3)
        await message.answer(search_result)
    except wikipedia.exceptions.DisambiguationError as e:
        await message.answer(f"Слишком много результатов найдено. Уточните ваш запрос: {e.options}")
    except wikipedia.exceptions.PageError:
        await message.answer("Страница не найдена.")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)