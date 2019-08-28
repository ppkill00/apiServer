#/usr/bin/python3

# schedule https://buildmedia.readthedocs.org/media/pdf/schedule/stable/schedule.pdf 
# Process https://docs.python.org/2/library/multiprocessing.html
# schedule jobs parallel https://schedule.readthedocs.io/en/stable/faq.html#how-to-execute-jobs-in-parallel
# multiprocess https://niceman.tistory.com/145?category=940952
# debug 를 사용하면 스레드가 2번 실행이 된다. 리로더의 문제인걸로 보인다. 

import schedule, signal, queue, threading,time, os, datetime,uuid
# from multiprocessing import Process
import multiprocessing

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



def sigint_handler(signum, frame):
    logger.warn('Stop pressing the CTRL+C!')
    logger.warn(str(signum))
    exit()
    pass

####################
# TODO define JOBS...

def job():
    logger.warn('i am here to die%s'%threading.current_thread())

schedule.every(2).seconds.do(job)


#####################

# @app.before_first_request
# def activate_job():
def run_job():
    while True:
        schedule.run_pending()
        time.sleep(1)




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
    thread = threading.Thread(target=run_job)
    thread.start()
    app.run(host='localhost', port=5000,debug=False)

