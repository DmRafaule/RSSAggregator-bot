from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware

with open(".env", "r") as file:
    buffer = file.read()
    line_pos = buffer.find("BOT_TOKEN")
    TOKEN = buffer[buffer.find("=", line_pos) + 1:buffer.find("\n", line_pos)]


bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
bot_dispatcher = Dispatcher(bot=bot)

# Set up translation
i18n = I18n(path="locales", domain="messages")
i18n_handler = SimpleI18nMiddleware(i18n)
i18n_handler.setup(bot_dispatcher)

WEBHOOK_URL = "https://timthewebmaster.com/{loc}/tools/rss-reader"