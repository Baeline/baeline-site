import asyncio
import os
from bot_handlers import riya, rivaa, tanisha, miyara, leya

async def run_bots():
    bots = [
        riya.get_app(os.getenv("BOT_TOKEN_RIYA")),
        rivaa.get_app(os.getenv("BOT_TOKEN_RIVAA")),
        tanisha.get_app(os.getenv("BOT_TOKEN_TANISHA")),
        miyara.get_app(os.getenv("BOT_TOKEN_MIYARA")),
        leya.get_app(os.getenv("BOT_TOKEN_LEYA")),
    ]
    await asyncio.gather(*(bot.run_polling() for bot in bots))

if __name__ == "__main__":
    asyncio.run(run_bots())
