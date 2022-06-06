#!/bin/bash

from aiogram import Bot, Dispatcher, executor, types
import python_weather
import asyncio

bot = Bot(token="5405416697:AAEePF8_vsjnfneU8CJjPlo949h4oOK7Fx8")
dp = Dispatcher(bot)
# declare the client. format defaults to metric system (celcius, km/h, etc.)
client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")

@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celsius = round((weather.current.temperature - 32) / 1.8)

    resp_msg = weather.location_name + "\n"
    resp_msg += f"Сегодня: {weather.current.sky_text}\n"
    resp_msg += f"{celsius}C°\n"

    for forecast in weather.forecasts:
        resp_msg += f"Прогноз на {forecast.date}\n"
        resp_msg += f"{forecast.sky_text}\n"
        resp_msg += f"{round((forecast.temperature - 32) / 1.8)}C°\n"

    await message.answer(resp_msg)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
