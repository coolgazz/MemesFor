from aiogram import Bot, Dispatcher, types, executor
import random

bot = Bot(token = '6899633318:AAF0dlOTxrIGkV2fcFG1JlJOlrUYp00Vv0E')
dp = Dispatcher(bot)
RESULTS = {
    "камень": {"ножницы": "Ты победил!", "бумага": "Ты проиграл!", "камень": "Ничья"},
    "ножницы": {"камень": "Ты проиграл!", "бумага": "Ты победил!", "ножницы": "Ничья"},
    "бумага": {"камень": "Ты победил!", "ножницы": "Ты проиграл!", "бумага": "Ничья"}
}

guess_number_secret = 0
guess_number_attempts = 0

# Функция для игры в "Камень-Ножницы-Бумагу"
@dp.message_handler(lambda message: message.text.lower() in ["камень", "ножницы", "бумага"])
async def play_rps(message: types.Message):
    options = ["камень", "ножницы", "бумага"]
    bot_choice = random.choice(options)
    user_choice = message.text.lower()

    await message.answer(f"Ты выбрал: {user_choice}. Я выбрал: {bot_choice}.")
    await message.answer(RESULTS[user_choice][bot_choice])

# Функция для игры в "Угадай число"
@dp.message_handler(lambda message: message.text.isdigit() and guess_number_secret != 0)
async def play_guess_number(message: types.Message):
    global guess_number_secret, guess_number_attempts

    user_number = int(message.text)
    guess_number_attempts += 1

    if user_number == guess_number_secret:
        await message.answer("Верно! Ты угадал число.")
        guess_number_secret = 0
        guess_number_attempts = 0
    else:
        if user_number > guess_number_secret:
            await message.answer("Число меньше.")
        else:
            await message.answer("Число больше.")

    if guess_number_attempts == 10:
        await message.answer(f"Ты проиграл! Правильный ответ: {guess_number_secret}.")
        guess_number_secret = 0
        guess_number_attempts = 0

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    keyboard.add(types.KeyboardButton("Играть в Камень-Ножницы-Бумагу"))
    keyboard.add(types.KeyboardButton("Играть в Угадай число"))
    await message.answer(
        "Привет! Я бот с играми и развлечениями. Выбери игру:",
        reply_markup=keyboard,
    )

# Обработка выбора игры
@dp.message_handler(lambda message: message.text in ["Играть в Камень-Ножницы-Бумагу", "Играть в Угадай число"])
async def choose_game(message: types.Message):
    global guess_number_secret
    if message.text == "Играть в Камень-Ножницы-Бумагу":
        keyboard = types.ReplyKeyboardRemove()
        await message.answer("Твой ход: камень, ножницы или бумага?", reply_markup=keyboard)
    elif message.text == "Играть в Угадай число":
        guess_number_secret = random.randint(1, 100)
        await message.answer("Угадай число от 1 до 100")

# Повторение сообщений пользователя
@dp.message_handler()
async def repeat_message(message: types.Message):
    await message.answer(f"Ты сказал: {message.text}")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)