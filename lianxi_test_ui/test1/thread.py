import threading
import time


exitflag = 1


class MyThread(threading.Thread):

    thread_lock = threading.Lock()
    threads = []

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = threadID
        self.thread_name = name
        self.counter = counter

    def run(self):
        print("线程开始： %s" % self.thread_name)
        self.thread_lock.acquire()
        print_time(self.name, self.counter, 5)
        self.thread_lock.release()
        print('结束线程: %s' % self.thread_name)


def print_time(threadName, delay, countor):
    while countor:
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        countor -= 1


if __name__ == '__main__':
    thread1 = MyThread(1, 'thread_1', 1)
    thread2 = MyThread(2, 'thread_2', 2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('结束线程')
