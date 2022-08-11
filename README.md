This is added to test pull-requests

Not enough

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
# Each month:
stromverbrauch.py plotall --password 0Vfe-ims7 --user strom --database stromverbrauch --host 192.168.1.11
stromverbrauch.py gettable --password 0Vfe-ims7 --user strom --database stromverbrauch --host 192.168.1.11 --table wasser | tail
stromverbrauch.py addone --password 0Vfe-ims7 --user strom --database stromverbrauch --host 192.168.1.11 --table wasser --zaehlerstand xxx
stromverbrauch.py gettable --password 0Vfe-ims7 --user strom --database stromverbrauch --host 192.168.1.11 --table stromsonst | tail
stromverbrauch.py addone --password 0Vfe-ims7 --user strom --database stromverbrauch --host 192.168.1.11 --table stromsonst --zaehlerstand xxx
stromverbrauch.py gettable --password 0Vfe-ims7 --user strom --database stromverbrauch --host 192.168.1.11 --table waermepumpe | tail
stromverbrauch.py addone --password 0Vfe-ims7 --user strom --database stromverbrauch --host 192.168.1.11 --table waermepumpe --zaehlerstand xxx
```

## Development
Add the development directory to the PYTHONPATH:
```
export PYTHONPATH=/home/eddgest/PycharmProjects/stromverbrauch/libs
```

## Testing
### Automated Testing
Run script to automatically
1. start and initialise a maria-DB container
2. run some commands against the stromverbrauch-DB
3. stop and delete the container again
```
./test-procedure.bash
```

### Manually Create a DB for testing
To quickly create a DB: [https://hub.docker.com/_/mariadb](https://hub.docker.com/_/mariadb)

Note: The docker-entrypoint-initdb.d directory is executed on startup and configures the DB
```
mysqldump --lock-tables -h 192.168.1.10 -u python_user -p0Vfe-ims7 stromverbrauch > /tmp/stromverbrauch-dbbackup_NUC_`date +"%Y%m%d"`.sql

docker run -d --rm --publish 127.0.0.1:3306:3306 \
    -e MYSQL_ROOT_PASSWORD=12test34 \
    -v /home/eddgest/PycharmProjects/stromverbrauch/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d \
    --name mariadb-test mariadb:latest
mysql -h"127.0.0.1" -P"3306" -u"root" -p"12test34" stromverbrauch < /tmp/stromverbrauch-dbbackup_NUC_20200214.sql

cd ~/PycharmProjects/stromverbrauch/
export PYTHONPATH=/home/eddgest/PycharmProjects/stromverbrauch/libs
./stromverbrauch.py plotall --host 127.0.0.1 --port 3306 --database stromverbrauch --password 12test34 --user python_user
```
to manually load the data:
```
mysql -h"127.0.0.1" -P"3306" -u"root" -p"12test34" stromverbrauch
create database stromverbrauch;
create user 'python_user'@'%' identified by '12test34';
grant all privileges on stromverbrauch.* to 'python_user'@'%' identified by '12test34';
flush privileges;
use stromverbrauch;
source stromverbrauch-dbbackup_NUC_`date +"%Y%m%d"`.sql

show grants for 'python_user'@'%';

mysql -h"127.0.0.1" -P"3306" -u"python_user" -p"12test34" stromverbrauch
show grants;
show triggers;
```

## Packaging
### Automated Packaging
Run script to automatically copy the files into place
```
./build-package.bash
```

### Manually build a package

## Command Examples
```
./stromverbrauch.py plotall --password 0Vfe-ims7 --user python_user --database stromverbrauch
./stromverbrauch.py addone --table wasser --password 0Vfe-ims7 --datum 2019-07-01 --zaehlerstand 675.0
./stromverbrauch.py addone --table stromsonst --password 0Vfe-ims7 --datum 2019-07-01 --zaehlerstand 18210.74
./stromverbrauch.py addone --table waermepumpe --password 0Vfe-ims7 --datum 2019-07-01 --zaehlerstand 15685.49
./stromverbrauch.py delone --table wasser --password 0Vfe-ims7 --host 192.168.1.10 --datum 2019-05-01
./stromverbrauch.py gettable --table wasser --password 0Vfe-ims7 --host 192.168.1.10
```
