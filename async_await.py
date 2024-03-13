import time

def task_one():
    t1=time.time()
    print(f"task_one started")
    time.sleep(5)
    print(f"task_one finished")
    t2=time.time()-t1
    return t2

def task_two():
    t1=time.time()
    print(f"task_two started")
    time.sleep(3)
    print(f"task_two finished")
    t2=time.time()-t1
    return t2
    

def execute_tasks():
    t1=time.time()
    print(f"task_one took {task_one()} secs")
    print(f"task_two took {task_two()} secs")
    print(f"total time = {time.time()-t1} secs")

execute_tasks()


print('#'*100)



import asyncio

async def task_one_():
    t1=time.time()
    print(f"task_one started")
    await asyncio.sleep(5)
    print(f"task_one finished")
    t2=time.time()-t1
    print(f"task_one took {t2} secs")

async def task_two_():
    t1=time.time()
    print(f"task_two started")
    await asyncio.sleep(3)
    print(f"task_two finished")
    t2=time.time()-t1
    print(f"task_two took {t2} secs")

async def execute_tasks_():
    t1=time.time()
    await asyncio.gather(task_one_(),task_two_())
    print(f"total time = {time.time()-t1} secs")

asyncio.run(execute_tasks_())