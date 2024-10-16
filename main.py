import asyncio
from aiogram import Bot, Dispatcher

from applocation.handler import router


async def main():
    bot = Bot(token="7938188972:AAFdCLfCaK0h_BSUbji5yJQkEc9JC36kaAk")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
      asyncio.run(main())