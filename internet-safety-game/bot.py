import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

# Токен вашего бота
API_TOKEN = '7513695715:AAGeGvvtQyTsa4yEHoQRRRPeVq7LDNc_FjE'

# Создаем экземпляры бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Кнопки
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Запустить игру")]  # Кнопка "Запустить игру"
    ],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(
        "Привет! Я бот, который поможет тебе изучить безопасность в интернете. Нажми кнопку, чтобы запустить игру!", 
        reply_markup=keyboard
    )

# Обработчик кнопки "Запустить игру"
@dp.message(lambda message: message.text == "Запустить игру")
async def launch_game(message: types.Message):
    try:
        # Запуск локальной игры через subprocess
        import subprocess
        subprocess.Popen(["python", "run_game.py"], shell=True)
        await message.answer("Игра запущена! Она откроется в браузере.")
    except Exception as e:
        await message.answer(f"Произошла ошибка при запуске игры: {e}")

# Обработчик других сообщений
@dp.message()
async def unknown_message(message: types.Message):
    await message.answer("Я понимаю только команды или кнопку запуска игры.")

# Основной запуск
async def main():
    print("Бот запущен...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
