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

To run your own functions you need to add then to the core/custom_lib.py file<br>
The engine makes use of 2 functions to send information and pings to the PHP client.

To send a new feed to the terminal<br>
```
core.addFeed(feed='Empty feed',thread_id=0)
```
Sends a new update status/ping to the thread<br>
```
core.sendUpdate(response='Response',thread=0)
```
<br>
<strong>Use global var 'thread' when creating an update or feed</strong>
<br>
Example function (also included in the base file):<br>
```
import time

def test():
	core.addFeed('test',thread)
	time.sleep(5)
```
<br>
After a function was completed the handler will return an completed status for 5 seconds before removing the thread
