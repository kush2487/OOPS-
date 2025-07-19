import threading
import time

def worker():
    print(f"Worker: thread starting - {threading.current_thread().name}")
    time.sleep(2)
    print(f"Worker: thread finished - {threading.current_thread().name}")


t1 = threading.Thread(target=worker, name="WorkerThread")
t2 = threading.Thread(target=worker, name="WorkerThread2")

t1.start()
t1.join()  # Wait for the first thread to finish
t2.start()

print("Main: thread is waiting for the worker thread to finish")

# t1.join() # Wait for the worker thread to finish

# print("Worker: thread has finished execution")
# print("Main: thread is exiting")









