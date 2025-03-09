import requests
import time
import asyncio
import aiohttp
from colorama import Fore, Style, init
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

init()

async def checker(username):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None)) as session:
        async with session.get(f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=2000-01-01") as response:
            x = await response.json()
            l = x.get("code")
            if l == 0:
                print(Fore.GREEN + f"VALID: {username}" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"TAKEN/???: {username}" + Style.RESET_ALL)

async def main():
    with open("usernames.txt", "r") as file:
        usernames = file.read().splitlines()

    tasks = [checker(username) for username in usernames]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
