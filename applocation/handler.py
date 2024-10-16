from aiogram import F,Router
from aiogram.filters import Command,CommandStart
from aiogram.types import Message

router = Router()
@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer("assalomu aleykum bratim!")

@router.message(Command('help'))
async def cmd_start(message:Message):
    await message.answer("bu bot tekin chat gpt bo`lib Xonimqulov Nodirbek tomonidan yaratilgan")

@router.message(Command('lang'))
async def cmd_start(message:Message):
    await message.answer("Tilni tanlang/выберайте язык/choose your language")


