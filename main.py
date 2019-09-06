# schedule https://buildmedia.readthedocs.org/media/pdf/schedule/stable/schedule.pdf 
# Process https://docs.python.org/2/library/multiprocessing.html
# schedule jobs parallel https://schedule.readthedocs.io/en/stable/faq.html#how-to-execute-jobs-in-parallel
# multiprocess https://niceman.tistory.com/145?category=940952
# debug 를 사용하면 스레드가 2번 실행이 된다. 리로더의 문제인걸로 보인다. 
# xhr https://stackoverflow.com/questions/8054165/using-put-method-in-html-form

import schedule, signal, queue, threading,time, os, datetime,uuid
# from multiprocessing import Process
import multiprocessing
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import logging
import logging.config
from webhooks import webhook

logging.config.fileConfig('./logging.conf', defaults={'logfilename': './automatorStatus.log'})
logger = logging.getLogger('automatorLogger')  
#logger.debug('debug message') 
#logger.info('info message') 
#logger.warn('warn message') 
#logger.error('error message') 
#logger.critical('critical message')

app = Flask(__name__)
Bootstrap(app)

app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
app.config['MYSQL_USER'] = os.environ['MYSQL_USERNAME'] 
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_USERPW'] 
app.config['MYSQL_DB'] = os.environ['MYSQL_DBNAME'] 

mysql = MySQL(app)

def sigint_handler(signum, frame):
    logger.warn('Stop pressing the CTRL+C!')
    logger.warn(str(signum))
    exit()
    pass

####################
# TODO define JOBS...

def job():
    #time.sleep(10)
    logger.warn('i am here to die %s'%threading.current_thread())

####################
# TODO define your schedules.
schedule.every(2).seconds.do(job)



#####################

# @app.before_first_request
# def activate_job():
def run_job():
    while True:
        schedule.run_pending()
        time.sleep(1)

threadPool =[]


@app.route('/', methods=['GET', 'POST'])
def index():
    cur = mysql.connection.cursor() 
    if request.method == 'POST':
        details = request.form
        applicationVersion = details['applicationVersion']
        email = details['email']
        assigner = details['assigner']
        cur.execute("INSERT INTO APP_RCPT_M(APPLICATIONVERSION, EMAIL_LIST,ASSIGNER) VALUES (%s, %s, %s)", (applicationVersion, email,assigner))
        mysql.connection.commit()
        cur.close()
        return render_template('redirect.html', message = '등록완료')
    cur.execute("SELECT APPLICATIONVERSION, EMAIL_LIST, ASSIGNER FROM APP_RCPT_M")
    datas = cur.fetchall()
    cur.close()
    return render_template('index.html',datas = datas,title = "Welcome Automator")

@app.route('/deleteApplication',methods=['POST'])
def deleteApplication():
    details = request.form
    applicationVersion = details['applicationVersion']
    print(applicationVersion)
    cur = mysql.connection.cursor() 
    cur.execute('DELETE FROM APP_RCPT_M WHERE APPLICATIONVERSION = \'' + applicationVersion + '\'')
    mysql.connection.commit()
    cur.close()
    return render_template('redirect.html', message = '제거완료')

@app.route('/whoami/<string:name>')
def whoami(name):
    return 'whoami page<br>' + name

# @app.route('/start')
# def startSchdule():
#     for i in threadPool:
#         if not i.isAlive():
#             run_job()
#     return "start program"

# @app.route('/end')
# def endSchedule():
#     for i in threadPool:
#         i.
#     # schedule.clear()
#     return "end program"
 

signal.signal(signal.SIGINT, sigint_handler)  #ctrl-c 예외 처리.


if __name__ == '__main__':
    ## 첫번째 argu는 스레드 함수 이름, 두번째 argu는 매개변수를 튜플 형태로 전달한 것.
#     thread = threading.Thread(target=run_job)
#     thread.start()
#     threadPool.append(thread)
    app.run(host='localhost', port=5000,debug=True)

