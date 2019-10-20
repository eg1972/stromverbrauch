create database stromverbrauch;
create user 'python_user'@'%' identified by '12test34';
grant all privileges on stromverbrauch.* to 'python_user'@'%' identified by '12test34';
flush privileges;
