import threading
import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


def thread_function(name, t): # This function is used to demonstrate threading
    time.sleep(t)
    print(f" {name}: starting")
    # time.sleep(2)
    print(f" {name}: finishing") 
    # return (f"Thread {name}: starting", f"Thread {name}: finishing")

def multithreaded_function(name, t): # This function is used to demonstrate multithreading
    print(f"Thread {name}: starting")
    time.sleep(t)
    print(f"Thread {name}: finishing")
#     return (f"Thread {name}: starting", f"Thread {name}: finishing")


def task(n):
    time.sleep(n)
    return f"Task {n} completed"




if __name__ == "__main__":
    '''This code demonstrates the use of threading and thread pools in Python.
    It creates a thread that sleeps for a specified time and then prints messages indicating the start and finish of the thread.
    It also uses a thread pool to manage multiple threads concurrently, allowing for efficient execution of tasks.'''

    time1 = time.perf_counter()

    print("Threading: starting thread")
    t1 = threading.Thread(target=thread_function, args=("Thread A",5))
    t1.start() # here we create a thread object, A is the name and 5 is the time to sleep
    t1.join() # here we wait for the thread to finish


    with ThreadPoolExecutor (max_workers=1) as executor: # Create a thread pool with 2 worker threads
        print("Threading: starting thread pool")
        executor.submit(thread_function, "Thread b", 4) # here we submit the thread function to the executor, A is the name and 4 is the time to sleep
        executor.submit(thread_function, "Thread c", 3) # here we submit the thread function to the executor, C is the name and 3 is the time to sleep
        executor.submit(thread_function, "Thread d", 2) # here we submit the thread function to the executor, D is the name and 2 is the time to sleep
        
        # Submit multiple tasks to the thread pool
        f1 = [executor.submit(task, i) for i in [3,4,5]]  
        for f in as_completed(f1):
            print(f.result())

    time2 = time.perf_counter()

    print("Main: all threads have been submitted")

    print(time2 - time1, "seconds elapsed")



    print("Main: starting multithreaded function")


    t2 = multiprocessing.Process(target=multithreaded_function, args=("A", 5))  # Create a process for the multithreaded function
    t2.start()  # Start the process
    t2.join()  # Wait for the process to finish

    ## Demonstrating the use of ProcessPoolExecutor for multiprocessing
    # This code demonstrates the use of ProcessPoolExecutor to run functions in separate processes.
    with ProcessPoolExecutor(max_workers=2) as executor:  # Create a process pool with 2 worker processes
        print("ProcessPoolExecutor: starting process pool")
        executor.submit(multithreaded_function, "A", 5)  # Submit a function to the process pool
        executor.submit(multithreaded_function, "B", 4)   # Submit another function to the process pool






