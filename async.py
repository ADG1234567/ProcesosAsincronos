import asyncio 
import time

async def function_1():
    for i in range(100000):
        if i % 50000 == 0:
            print('Helllo from function_1\n')
            print ( i - 25)
            await asyncio.sleep(3.3)
            print ( i - 50)
            await asyncio.sleep(3.3)
            print ( i - 75)
            await asyncio.sleep(3.3)
            # Pause the execution
            await asyncio.sleep(3.3)
    return 0

async def function_2():
    cont = 0
    while cont < 5:
        print('>>> I am from function_2 \n')
        print(cont)
        cont += 1
        await asyncio.sleep(1)  # Add a small delay to make the output more visible
    return 0

async def main():
    f1 = loop.create_task(function_1())
    f2 = loop.create_task(function_2())
    await asyncio.wait([f1, f2])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()