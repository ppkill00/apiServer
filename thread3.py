import queue
import time
import threading
import schedule


def job():
    print("I'm working %s "% threading.current_thread())


def worker_main():
    while 1:
        job_func = jobqueue.get()
        job_func()
        jobqueue.task_done()

jobqueue = queue.Queue()

schedule.every(2).seconds.do(jobqueue.put, job)
schedule.every(2).seconds.do(jobqueue.put, job)
schedule.every(2).seconds.do(jobqueue.put, job)
schedule.every(2).seconds.do(jobqueue.put, job)
schedule.every(2).seconds.do(jobqueue.put, job)

worker_thread = threading.Thread(target=worker_main)
worker_thread.start()

while 1:
    schedule.run_pending()
    time.sleep(1)