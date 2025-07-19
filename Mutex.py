import threading

a = 0


def add():
    global a
    for i in range(1000000000):
        a += 1

def sub():
    global a
    for i in range(1000000000):
        a -= 1


t1 = threading.Thread(target=add)
t2 = threading.Thread(target=sub)   


t1.start()
t2.start()


t1.join()
t2.join()

print(a)  # This should print 0 if the threads worked correctly