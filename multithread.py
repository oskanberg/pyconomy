from multiprocessing import Process, Lock

def processData(i, mutex):
    print i
    

if __name__ == '__main__':
    mutex = Lock()
    threads = list()
    for i in range(10):
        threads.append(Process(target = processData, args = (i, mutex)))
        threads[len(threads) - 1].start()
    for thread in threads:
        thread.join()

