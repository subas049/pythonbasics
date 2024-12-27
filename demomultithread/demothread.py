import threading
import time


def Updatedb():
    print("Updating db ....")
    time.sleep(10)
    print("db updated ....")


def Updatenum(n):
    for i in range(1, n + 1):
        print(i)


# Updatedb()
threadfordb = threading.Thread(target=Updatedb)
threadfordb.start()

Updatenum(100)

print(threading.active_count())
print(threading.enumerate())

threadfordb.join()
print("Bye")
