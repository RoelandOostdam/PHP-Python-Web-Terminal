##PHP/Python Web Terminal - A threaded PHP to Python Protocol

![alt text](https://preview.ibb.co/i6V0HH/terminal.png)

Requirements:<br>
-<a href='https://pypi.python.org/pypi/MySQL-python/1.2.5'>Python MySQLDB</a>

## Installation
-Import database from SQL/terminal_data.sql<br>
-Change database configuration in /Python/config.cfg<br>
-Change database configuration in /PHP/config.cfg<br>

## Usage
<strong>System commands stored in core.py</strong><br>
cls() - Clears console<br>
flush() - Flushes all threads used to remove unresponsive threads<br>
cflush() - Does the above commands
<br>
<strong>Execute terminal.py on server to start the listener</strong><br>
