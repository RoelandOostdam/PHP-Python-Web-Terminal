##PHP/Python Web Terminal - A threaded PHP to Python Protocol

![alt text](https://preview.ibb.co/i6V0HH/terminal.png)

Requirements:<br>
-<a href='https://www.python.org/downloads/'>Python 2.7</a><br>
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
```python
core.addFeed(feed='Empty feed',thread_id=0)
```
To send a new update status/ping to the thread. Note that unresponsive threads will be hidden from the client after 60 seconds (the function will not be terminated)<br>
```python
core.sendUpdate(response='Response',thread=0)
```
<strong>Use global var 'thread' when creating an update or feed</strong>
<br>
Example functions (also included in the base file):<br>
```python
import time
#-------------------------------------------------------------------------------------#
#example function that directly executes a python command and returns its true output
def pyExec(command):
	try:
		output = eval(command)
		if(output==None):
			output = 'Empty response'
		print 'Output = '+str(output)
		core.addFeed(str(output),thread)
	except Exception as e:
		core.addFeed('Error in thread '+str(thread)+' executing '+command+': '+str(e),thread)
#example function that returns a feed
def test(text='test'): 
	core.addFeed(str(text),thread)
	time.sleep(5)
```
The above function can be executed in the terminal by using:
```python
pyExec(test("the answer is: "+str(10/2)))
#returns 'the answer is: 5'
```
<strong>Make sure to use double quotes to call a function</strong><br>
After a function was completed the handler will return an completed status for 5 seconds before removing the thread
