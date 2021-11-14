import random
import threading
import time

numberOfThreads = 5
choosing = [False for i in range(numberOfThreads)]
ticket = [0 for i in range(numberOfThreads)]


def run(id):
    for i in range(5):
        lock(id)
        time.sleep(random.random())
        unlock(id)
def lock(id):
    choosing[id] = True
    ticket[id] = findMax() + 1
    choosing[id] = False
    print("Thread ", id, " got ticket in Lock")

    for j in range(numberOfThreads):
        if j == id:
            continue

        # wait if thread is choosing
        while choosing[j]:
            choosing[j] = True

        while ticket[j] != 0 and (ticket[id] > ticket[j] or (ticket[id] == ticket[j] and id > j)):
            x = True

def unlock(id):
    ticket[id] = 0


def findMax():
    m = ticket[0]
    for i in range(1, numberOfThreads):
        if ticket[i] > m:
            m = ticket[i]
    return m


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    threads = []

    for i in range(numberOfThreads):
        threads.append(threading.Thread(target=run, args=(i,)))
        threads[i].start()

    for i in range(numberOfThreads):
        threads[i].join()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
