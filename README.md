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
