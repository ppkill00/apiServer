#/bin/sh

#mysql setting
export ADMIN_PASS='ajtmf3376'
export MYSQL_USERNAME='secucenter'
export MYSQL_USERPW='!qhdkstpsxj!'
export MYSQL_DBNAME='management_db'
export MYSQL_HOST='0.0.0.0'

#hook 설정
export HOOKURL='https://hooks.slack.com/services/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'



# Core/config/reports 의 템플릿에 수치 제한 5를 -1 무한으로 세팅해야함. 

#export NLS_LANG=KOREAN_KOREA.KO16KSC5601 #한글 이슈 해결
#export ORACLE_HOME=/home/wulf/instantclient_18_3 #오라클 홈
#export PATH=$PATH:/home/wulf/instantclient_18_3 #오라클 패스
#export LD_LIBRARY_PATH=$ORACLE_HOME #오라클 실행라이브러리 패스 



# 최초시 아래 설정
# clear

# echo "=================================================================="
# echo "                        MySQL useradd"
# echo "=================================================================="
# echo "Username : $MYSQL_USERNAME"
# echo "dbname : $MYSQL_DBNAME"
# echo -n "User p/w : $MYSQL_USERPW"
# echo ""


# read userpw

#before 8
# echo " " >> mysql_useradd.sql
# echo "use mysql" >> mysql_useradd.sql
# echo "create database $MYSQL_DBNAME;" >> mysql_useradd.sql
# echo "GRANT ALL PRIVILEGES ON $MYSQL_DBNAME.* to $MYSQL_USERNAME@localhost IDENTIFIED BY '$MYSQL_USERPW' with grant option;" >> mysql_useradd.sql
# echo "GRANT ALL PRIVILEGES ON $MYSQL_DBNAME.* TO $MYSQL_USERNAME@% IDENTIFIED BY '$MYSQL_USERPW' with grant option;" >> mysql_useradd.sql
# echo "FLUSH PRIVILEGES;" >> mysql_useradd.sql
#after 8
# echo " " >> mysql_useradd.sql
# echo "use mysql" >> mysql_useradd.sql
# # echo "create database $MYSQL_DBNAME;" >> mysql_useradd.sql
# echo "CREATE USER '$MYSQL_USERNAME'@'%' IDENTIFIED BY '$MYSQL_USERPW';" >> mysql_useradd.sql
# echo "GRANT ALL PRIVILEGES ON $MYSQL_DBNAME.* TO '$MYSQL_USERNAME'@'%' WITH GRANT OPTION;" >> mysql_useradd.sql
# echo "FLUSH PRIVILEGES;" >> mysql_useradd.sql


# mysql -h 0.0.0.0 -uroot -p$ADMIN_PASS < ./mysql_useradd.sql
# mysql -h 0.0.0.0 -u$MYSQL_USERNAME -p$MYSQL_USERPW < ./mysql_table.sql
# mysql -h 0.0.0.0 -u$MYSQL_USERNAME -p$MYSQL_USERPW < ./temp.sql

# cat ./mysql_useradd.sql
# rm -rf ./mysql_useradd.sql

