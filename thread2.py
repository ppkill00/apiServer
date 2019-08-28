import queue
import time
import threading
import schedule


def job():
    print("I'm working but lazy %s "% threading.current_thread())
    time.sleep(5)
    print("i'm done lazy man. %s "% threading.current_thread())

def job2():
    print("i dont want to working %s " % threading.current_thread())


def worker_main():
    while 1:
        job_func = jobqueue.get()
        job_func()
        jobqueue.task_done()

jobqueue = queue.Queue()

schedule.every(2).seconds.do(jobqueue.put, job)
schedule.every(2).seconds.do(jobqueue.put, job2)

worker_thread = threading.Thread(target=worker_main)
worker_thread.start()

while 1:
    schedule.run_pending()
    time.sleep(1)