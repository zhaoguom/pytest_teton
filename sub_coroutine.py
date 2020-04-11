import asyncio

async def compute(x, y):
    print("processing: {}, {}...".format(x, y))
    await asyncio.sleep(2.0)
    return x+y

async def sum(x, y):
    result = await compute(x, y)
    print("{} + {} = {}".format(x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(sum(1,2))
loop.close()