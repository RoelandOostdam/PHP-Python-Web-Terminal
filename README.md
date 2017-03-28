## PoPPeR - PHP to Python Protocol
<br><p align="center"><img src="https://www.dropbox.com/s/t8qqhsiwlbiee13/popper.PNG?dl=1"></p>
<br>


Requirements:<br>
-Python MySQLDB

## Installation
Import python_data.sql as database<br>
Change database configuration in /Python/master_lib.py
```python
def db_connect():
	global ip, user, password, dbn, db
	ip = "localhost"
	user = "root"
	password = ""
	dbn = "python_data"

	return MySQLdb.connect(ip,user,password,dbn)
```
Change database configuration in /PHP/conn.py
```php
$ip = 'localhost';
$user = 'root';
$pass = '';
$db = 'python_data';
```
If you want to load configuration from files
```php
$fp = fopen('config/conn_ip', 'r');
$ip = fread($fp, filesize('config/conn_ip'));

$fp = fopen('config/conn_user', 'r');
$user = fread($fp, filesize('config/conn_user'));

$fp = fopen('config/conn_pass', 'r');
$pass = fread($fp, filesize('config/conn_pass'));

$fp = fopen('config/conn_db', 'r');
$db = fread($fp, filesize('config/conn_db')-1);
```

## Usage
<strong>Commands located in master_lib.py</strong><br>
cls() - clears console<br>
version() - displays master_lib version<br>
threader(file) - starts threaded script<br>
handle() - starts threaded handler<br>
execute(command, arg1, arg2, arg3) - executes python command e.g. print<br>
<br>
<strong>Execute python_master_handler.py on server to start the listener</strong><br>
