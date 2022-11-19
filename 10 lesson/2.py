from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp
from asyncio import create_task

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(service):
    # получение ip
    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as resp:
            json = await resp.json()
            return json[service.ip_attr]


async def asynchronous(tuple):
    p = []
    for st in tuple:
        task = create_task(fetch_ip(st))
        p.append(task)
    await asyncio.wait(p, return_when = asyncio.FIRST_COMPLETED)


asyncio.run(asynchronous(SERVICES))