import asyncio
import sys

sys.path.append(r"E:\projects\Python\git-proj\melobot")
from melobot.models.session import BotSession, SessionLocal

local = SessionLocal()
local: BotSession


async def main():
    print(local.timestamp)


asyncio.run(main())
