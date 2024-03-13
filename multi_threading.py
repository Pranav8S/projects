from threading import Thread, Lock
import os
import time
import random

print(f"start main")
t1=time.time()

# list to store all the threads
threads= []

# get the cpu core count
num_threads= os.cpu_count()

n=0
x=0
lock = Lock()


# random sample function
def example_function():
    global n
    t1=time.time()
    
    for _ in range(100000):
        random.randint(1,1000) ** random.randint(1,1000) #type: ignore
    time.sleep(1)
    t2=time.time()

    with lock: # this is a more convinient way of lock than using a wrapper which locks using acquire() and release() as this takes care of both
        print(f"thread no {n} took {t2-t1} secs") # if we encounter multiple threads with same number this simulates a race condition
        n+=1
    
# creating threads ;; here we are creating threads for the same function
for i in range(num_threads): #type: ignore
    t = Thread(target=example_function) # target is the code we want to multitask
    threads.append(t)


# for below part see the difference by running and debugging this code

# first case
# for the case where resources are shared or one thread should only execute after previous one ends
# staring all the threads one after other
# for t in threads:
#     print(f"thread no {x} started")
#     x+=1
#     t.start()
#     t.join() # this tells python that one thread should run only after the previous is finished

# second case
# for the case where threads are idependent of one other and concurrent starting doesnt affect the program we can define start and end in seperate functions
for t in threads:
    print(f"thread no {x} started")
    x+=1
    t.start()

for t in threads:
     t.join()



print(f"end main")
t2=time.time()

print(f"total time= {t2-t1} secs")
