import asyncio


async def print_numbers():
    num = 1
    while True:
        print(num)
        await asyncio.sleep(0.5)
        num += 1


async def print_time():
    time = 0
    while True:
        if time != 0 and time % 3 == 0:
            print("{} seconds from beginning".format(time))
        await asyncio.sleep(1)
        time += 1


async def main():
    task1 = asyncio.ensure_future(print_numbers())
    task2 = asyncio.ensure_future(print_time())
    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(main())
