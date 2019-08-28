import threading
import time
import schedule



def job():
    print("I'm working but lazy %s "% threading.current_thread())
    time.sleep(10)
    print("i'm done lazy man. %s "% threading.current_thread())

def job2():
    print("JOB 2 %s " % threading.current_thread())


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(2).seconds.do(run_threaded, job)
schedule.every(2).seconds.do(run_threaded, job2)



while 1:
    schedule.run_pending()
    time.sleep(1)