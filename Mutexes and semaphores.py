import threading

import time

'''
||||||------------Mutexes-------------------||||
'''

lock = threading.Lock()
shared_resource = 0

def increment(name):
    global shared_resource
    print(f"{name} wants a lock")

    lock.acquire()

    try:
        print(f"{name} has a lock")
        local = shared_resource
        time.sleep(0.1)  # Simulate some work
        local += 1
        shared_resource = local
        print(f"{name} incremented shared_resource to {shared_resource}")
    finally:
        print(f"{name} releasing lock")
        lock.release()

threads = [threading.Thread(target=increment, args=(f"Thread-{i}",)) for i in range(5)]

for i in threads:
    print(f"Starting {i.name}")
    i.start()  
for j in threads:
    print(f"Joining {j.name}")
    j.join()

print("--------------------------------------------------")
print("--------------------------------------------------")
print("--------------------------------------------------\n")

'''
||||||------------Semaphores-------------------||||

'''


semaphore = threading.Semaphore(2)  # Allow 2 threads to access the resource at a time

def access_resource(name):
    print(f"{name} trying to acquire semaphore")
    semaphore.acquire()
    try:
        print(f"{name} acquired semaphore")
        time.sleep(1)  # Simulate some work
    finally:
        print(f"{name} releasing semaphore")
        semaphore.release()

threads_semaphore = [threading.Thread(target=access_resource, args=(f"Thread-{i}",)) for i in range(5)]
for i in threads_semaphore:
    print(f"Starting semaphore  {i.name}\n")
    i.start()  
for j in threads_semaphore:
    print(f"Joining semaphore  {j.name}\n")
    j.join() 

    