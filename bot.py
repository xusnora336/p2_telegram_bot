import asyncio
import os

from aiogram.filters import CommandStart, Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Button"),
        KeyboardButton(text="Yordam"),
        KeyboardButton(text="Button3"),
    ],
    [
        KeyboardButton(text="Button4"),
        KeyboardButton(text="Button5"),
        KeyboardButton(text="Button6"),
    ]
])

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Inline Keyboard", callback_data="Test"),
         InlineKeyboardButton(text="Inline Keyboard2", callback_data="Test2", url="https://telegram.org")]
    ]
)


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Salom", reply_markup=keyboard)


@dp.message(Command("help"))
async def _help(message: types.Message):
    await message.answer("Help", reply_markup=inline_keyboard)


@dp.message(F.text == "Yordam")
async def _filter(message: types.Message):
    await message.answer(f"Nima yordam kerak?")



async def main():
    print("Starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
