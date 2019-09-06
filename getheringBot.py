
import json,os
import requests, urllib.parse,subprocess,time
from requests.auth import HTTPBasicAuth
from requests_toolbelt.utils import dump
from webhooks import webhook
import logging

logger = logging.getLogger('automatorLogger') 


headers = {'content-type':'application/x-www-form-urlencoded','Accept':'application/json, text/javascript, */*; q=0.01',
'Referer':'https://recommend.wisereport.co.kr/v1/Home/RecommendSummary/naver','Sec-Fetch-Mode':'cors','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.71 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'}

url = 'https://recommend.wisereport.co.kr/v1/Home/TopRecommend'
data = 'proc=3&dt=20190829'

resp = requests.post(url,headers=headers, data=data) #한글빼고 잘댐

dumpData = dump.dump_all(resp)
print(dumpData.decode('utf-8'))

if resp.status_code >= 200:
    if resp.status_code < 300:
        logger.debug('status : ' + str(resp.status_code))
        try:
            json_data = json.loads(resp.text)
            print(json.dumps(json_data,sort_keys = True, indent = 4))
            webhook(json_data,None,None)
            # return(json_data['key'])
        except:
            logger.debug('Request of jiraApiPost')
    else:
        webhook("Jira Api Error : " + str(resp.status_code) +resp.text,None,None)
        logger.error(resp.text)
