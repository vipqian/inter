import os
from multiprocessing import Process

# if __name__ == '__main__':
#     print(os.getpid())
#     pid = os.fork()
#     if pid < 0:
#         print('error')
#     elif pid == 0:
#         print('I am child process %s and my parent process is %s' % (os.getpid(), os.getppid()))
#     else:
#         print('I(%s) created a process (%s)' % (os.getpid(), pid))


def run_proc():
    print('Child process %s' % os.getpid())
if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print('Process will start')
        p.start()
    p.join()
    print('Process end')