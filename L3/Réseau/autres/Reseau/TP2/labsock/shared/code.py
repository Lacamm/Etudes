import asyncio
import time

async def affiche(msg, delai):
    await asyncio.sleep(delai)
    print(msg)

async def attente():
    await affiche('Hello', 5)
    await affiche('World', 2)

async def concurente():
    task1 = asyncio.create_task(affiche('hello', 5))
    task2 = asyncio.create_task(affiche('world', 2))
    await task1
    await task2

print(f"started at {time.strftime('%X')}")
asyncio.run(attente())
print(f"finished at {time.strftime('%X')}")

print(f"started at {time.strftime('%X')}")
asyncio.run(concurente())
print(f"finished at {time.strftime('%X')}")
