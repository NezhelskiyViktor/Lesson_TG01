import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, KEY
import requests
from googletrans import Translator


def get_weather(city):
    api_key = KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    t = round(data['main']['temp'])
    text = data['weather'][0]['description']
    print(text)

    translator = Translator()
    weather = translator.translate(text, src='en', dest='ru').text
    print(weather)

    return f"Сейчас в Москве: t = {t}°C\nПогода: {weather}"


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def start(message: Message):
        await message.answer("Приветики, я бот!")

    @dp.message(Command('help'))
    async def help(message: Message):
        await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")

    @dp.message(F. text == "погода")
    async def aitext(message: Message):
        await message.answer(get_weather('Moscow'))

    await dp.start_polling(bot)


    async def main():
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

