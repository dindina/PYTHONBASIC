import threading
import time

def task(name):
    print(f"Thread {name} : starting")
    counter = 1
    while counter < 10:
        print(f"Thread {name} : sleeping")
        time.sleep(2)
        counter += 1
    print(f"Thread {name} : finished")


if __name__ == "__main__":
    thread1 = threading.Thread(target=task , args=("Thread1",) )
    thread2 = threading.Thread(target=task, args=("Thread2",) )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


