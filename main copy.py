import schedule,signal
import time
import datetime
import uuid

from flask import Flask, request
from multiprocessing import Process
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

def run_job(id):
    """ sample job with parameter """
    global job_timer
    print("timer job id={}".format(id))
    print("timer: {:.4f}sec".format(time.time() - job_timer))
    job_timer = time.time()

def run_schedule():
    """ infinite loop for schedule """
    global job_timer
    job_timer = time.time()
    while 1:
        schedule.run_pending()
        time.sleep(1)

@app.route('/')
def index():
    global t, job_timer
    return 'index page<br>' +str(time.ctime())

@app.route('/timer/<string:status>')
def mytimer(status, nsec=10):
    global t, job_timer
    if status=='on' and not t:
        schedule.every(nsec).seconds.do(run_job, str(uuid.uuid4()))
        t = Process(target=run_schedule)
        t.start()
        return "timer on with interval:{}sec\n".format(nsec)
    elif status=='off' and t:
        if t:
            t.terminate()
            t = None
            schedule.clear()
        return "timer off\n"
    return "timer status not changed\n"

if __name__ == '__main__':
    app.run(host='localhost', port=5000,debug=True)


signal.signal(signal.SIGINT, sigint_handler)  #ctrl-c 예외 처리.