from multiprocessing import Process, Lock, Value
import os
import time
import random

# random sample function
def example_function(n):
    t1=time.time()
    
    for _ in range(100000):
        random.randint(1,1000) ** random.randint(1,1000) #type: ignore
    time.sleep(5)
    t2=time.time()

    print(f"process no {n} took {t2-t1} secs")

    
if __name__ =='__main__':

    print(f"start main")
    t1=time.time()

    # list to store all the processes
    processes= []

    # get the cpu core count
    num_processes= os.cpu_count()

    # creating threads ;; here we are creating process for the same function
    for i in range(num_processes): #type: ignore
        p = Process(target=example_function, args=(i,)) # target is the code we want to multitask
        processes.append(p)

    for i,p in enumerate(processes):
        print(f"process no {i} started")
        p.start()
        
    for p in processes:
        p.join()

    print(f"end main")
    t2=time.time()

    print(f"total time= {t2-t1} secs")




