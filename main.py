#!/usr/bin/env python

import asyncio
import logging
import sys

from aiogram import types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from config import bot_dispatcher, bot, WEBHOOK_URL


@bot_dispatcher.message(Command('help'))
async def help(message: Message):
    markup = InlineKeyboardBuilder()
    locale = message.from_user.language_code
    url = WEBHOOK_URL.format(loc=locale)
    markup.button(text='RSSReader', web_app=types.WebAppInfo(url=url))
    await message.answer(_("Этот бот является простой интеграцией моего веб инструмента <b>RSSReader</b> в Телеграмме"))
    await message.answer(_("/startapp - запустить приложение"), reply_markup=markup.as_markup(resize_keyboard=True))

@bot_dispatcher.message(Command("startapp"))
async def start_app(message: Message):
    markup = InlineKeyboardBuilder()
    locale = message.from_user.language_code
    url = WEBHOOK_URL.format(loc=locale)
    markup.button(text=_('Открыть'), web_app=types.WebAppInfo(url=url))
    await message.answer("RSSReader", reply_markup=markup.as_markup(resize_keyboard=True))


async def main() -> None:
    await bot_dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
