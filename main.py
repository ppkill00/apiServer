#/usr/bin/python3

# schedule https://buildmedia.readthedocs.org/media/pdf/schedule/stable/schedule.pdf 
# Process https://docs.python.org/2/library/multiprocessing.html
# schedule jobs parallel https://schedule.readthedocs.io/en/stable/faq.html#how-to-execute-jobs-in-parallel
# multiprocess https://niceman.tistory.com/145?category=940952

import schedule, signal, queue, threading,time, os, datetime,uuid
from multiprocessing import Process

from flask import Flask, request
import logging
import logging.config


logging.config.fileConfig('./logging.conf', defaults={'logfilename': './automatorStatus.log'})
logger = logging.getLogger('automatorLogger')  
#logger.debug('debug message') 
#logger.info('info message') 
#logger.warn('warn message') 
#logger.error('error message') 
#logger.critical('critical message')

app = Flask(__name__)

t = None
job_timer = None


def sigint_handler(signum, frame):
    logger.warn('Stop pressing the CTRL+C!')
    logger.warn(str(signum))
    exit()
    pass

####################
# TODO define JOBS...

def job():
    logger.warn('i am here to die%s'%threading.current_thread())
    print('test')

#####################



def worker_main():
    while 1:
        job_func = jobqueue.get()
        job_func()
        jobqueue.task_done()

jobqueue = queue.Queue()


worker_thread = threading.Thread(target=worker_main)
worker_thread.start()

def run_schedule():
    """ infinite loop for schedule """
    print('start schedule')
    while 1:
        schedule.run_pending()
        time.sleep(1)




schedule.every(2).seconds.do(job)


if os.environ['ENV'] == "DEV":
    schedule.every(2).seconds.do(jobqueue.put, job)
    #schedule.every(5).seconds.do(batchJob().startAllBatch) #30min
    #schedule.every(10).seconds.do(developerReport.createCont)



@app.route('/')
def index():
    return 'start schedule index page<br>' +str(time.ctime())


@app.route('/whoami/<string:name>')
def whoami(name):

    return 'whoami page<br>' + name


@app.route('/end')
def mytimer():
    schedule.clear()
    return "end program"
 


signal.signal(signal.SIGINT, sigint_handler)  #ctrl-c 예외 처리.


if __name__ == '__main__':
    p = Process(target=app.run(host='localhost', port=5000,debug=True))
    t = Process(target=run_schedule)
    t.start()

    p.start()
    t.join()

    p.join()

