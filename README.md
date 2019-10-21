# stromverbrauch
This application serves as a front-end for the database
holding the data.

The front end can:
1. retrieve and print the data
2. add data 
3. plot data
4. remove data

## Monthly maintenance
```
Each month:
cd /home/eddgest/PycharmProjects/stromverbrauch
./stromverbrauch.py addone --host 192.168.1.10 --table wasser --password 0Vfe-ims7 --zaehlerstand 649
./stromverbrauch.py gettable --table wasser --password 0Vfe-ims7 --host 192.168.1.10|tail
./stromverbrauch.py addone --host 192.168.1.10 --table stromsonst --password 0Vfe-ims7 --zaehlerstand 17553.98
./stromverbrauch.py gettable --table stromsonst --password 0Vfe-ims7 --host 192.168.1.10|tail
./stromverbrauch.py addone --host 192.168.1.10 --table waermepumpe --password 0Vfe-ims7 --zaehlerstand 15456.76
./stromverbrauch.py gettable --table waermepumpe --password 0Vfe-ims7 --host 192.168.1.10|tail
./stromverbrauch.py plotall --password 0Vfe-ims7 --user python_user --database stromverbrauch
```

## Create a DB for testing
To quickly create a DB:
https://hub.docker.com/_/mariadb

```
mysqldump --lock-tables -h 192.168.1.10 -u java_user -p0Vfe-ims7 java_test > /mnt/data-aldi-admin/gereon/backup/mysql-backup/java_test-dbbackup_NUC_`date +"%Y%m%d"`.bak

docker run -d --rm --publish 127.0.0.1:3306:3306 \
    -e MYSQL_ROOT_PASSWORD=12test34 \
    -v /home/eddgest/PycharmProjects/stromverbrauch/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d \
    --name mariadb-test mariadb:latest

mysql -h"127.0.0.1" -P"3306" -u"root" -p"12test34" stromverbrauch
create database stromverbrauch;
create user 'python_user'@'%' identified by '12test34';
grant all privileges on stromverbrauch.* to 'python_user'@'%' identified by '12test34';
flush privileges;
use stromverbrauch;
source 6-mysql_java_test_dump.sql

show grants for 'python_user'@'%';

mysql -h"127.0.0.1" -P"3306" -u"python_user" -p"12test34" stromverbrauch
show grants;
show triggers;
```

## Examples
```
./stromverbrauch.py plotall --password 0Vfe-ims7 --user python_user --database stromverbrauch
./stromverbrauch.py addone --table wasser --password 0Vfe-ims7 --datum 2019-07-01 --zaehlerstand 675.0
./stromverbrauch.py addone --table stromsonst --password 0Vfe-ims7 --datum 2019-07-01 --zaehlerstand 18210.74
./stromverbrauch.py addone --table waermepumpe --password 0Vfe-ims7 --datum 2019-07-01 --zaehlerstand 15685.49
./stromverbrauch.py delone --table wasser --password 0Vfe-ims7 --host 192.168.1.10 --datum 2019-05-01
./stromverbrauch.py gettable --table wasser --password 0Vfe-ims7 --host 192.168.1.10
```
