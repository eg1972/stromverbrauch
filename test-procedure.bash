#!/bin/bash

rootpw="12test34"
containername=mariadb-test
DATE="2019-05-01"

echo "create DB-container"
docker run --rm -d --publish 127.0.0.1:3306:3306 \
    -e MYSQL_ROOT_PASSWORD=${rootpw} \
    -v /home/eddgest/PycharmProjects/stromverbrauch/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d \
    --name ${containername} mariadb:latest > /dev/null 2>&1

#mysql -h"127.0.0.1" -P"3306" -u"python_user" -p"12test34" stromverbrauch
sleep 10

echo "run tests"
./stromverbrauch.py gettable --host 127.0.0.1 --port 3306 --database stromverbrauch --user python_user --password 12test34 --table stromsonst | tail | grep $DATE > /dev/null 2>&1
res1=$?
./stromverbrauch.py addone --host 127.0.0.1 --port 3306 --database stromverbrauch --user python_user --password 12test34 --table stromsonst --datum ${DATE} --zaehlerstand 17554.12 --preis 0.2463 > /dev/null 2>&1
res2=$?
./stromverbrauch.py gettable --host 127.0.0.1 --port 3306 --database stromverbrauch --user python_user --password 12test34 --table stromsonst | tail | grep $DATE > /dev/null 2>&1
res3=$?
./stromverbrauch.py delone --host 127.0.0.1 --port 3306 --database stromverbrauch --user python_user --password 12test34 --table stromsonst --datum ${DATE} > /dev/null 2>&1
res4=$?
./stromverbrauch.py gettable --host 127.0.0.1 --port 3306 --database stromverbrauch --user python_user --password 12test34 --table stromsonst | tail | grep $DATE > /dev/null 2>&1
res5=$?

#./stromverbrauch.py plotall --host 127.0.0.1 --port 3306 --database stromverbrauch --user python_user --password 12test34
echo "evaluate results"
if [ $res1 == 1 ] && [ $res2 == 0 ] && [ $res3 == 0 ] && [ $res4 == 0 ] && [ $res5 == 1 ]
then
  echo "= OK => all tests passed"
  echo "stopping and deleting DB-container"
  docker stop ${containername} > /dev/null 2>&1
  exit 0
else
  echo "= NOK => some tests failed"
  echo "stopping and deleting DB-container"
  docker stop ${containername} > /dev/null 2>&1
  exit 1
fi

