import aiohttp
import asyncio
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def run():
    url = "http://shop.projectsedu.com/goods/{}/"
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(1,50):
            task = asyncio.ensure_future(fetch(session, url.format(i)))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        print(responses)

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    print("elapsed time: {}".format(time.time()-start_time))