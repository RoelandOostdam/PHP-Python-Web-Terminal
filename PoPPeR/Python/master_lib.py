## @package master_lib
## \brief All the php web-console to python functions are listed in this library
"""
All the php web-console to python functions are listed in this library
"""
import subprocess, time, datetime, StringIO
import MySQLdb, status_handler
import time, datetime, os, sys, random
import master_lib
from threading import Thread
import __builtin__

__builtin__.debug=0

def db_connect():
	"""Connects to the python db"""
	global ip, user, password, dbn, db
	ip = "localhost"
	user = "oemraw"
	password = "Ramdew123Curry"
	dbn = "python_data"

	return MySQLdb.connect(ip,user,password,dbn)

def db_connect_overcast():
	"""Connects to the overcast db"""
	global ip, user, password, dbn, db
	ip = "localhost"
	user = "oemraw"
	password = "Ramdew123Curry"
	dbn = "overcast_db"

	return MySQLdb.connect(ip,user,password,dbn)

def cls():
	"""Clears terminal screen"""
	db = db_connect()
	cursor = db.cursor()
	cursor.execute("TRUNCATE python_master_console")
	db.commit()
	cursor.close()

def update_console(line, spec='none'):
	"""Updates console with user input"""
	db = db_connect()
	cursor = db.cursor()
	if spec=='none':
		cursor.execute("INSERT INTO python_master_console (console_time,console_line) VALUES ('" + status_handler.timestamp() + "','" + str(line) + "')")
	else:
		line = "##USER_INPUT: " + str(line)
		cursor.execute("INSERT INTO python_master_console (console_time,console_line) VALUES ('" + status_handler.timestamp() + "','" + str(line) + "')")
	db.commit()
	cursor.close()

def version():
	"""Returns the master_lib version"""
	version = 'PMH running on master_lib 2.4'
	print version
	update_console(version)

def threader(file):
	"""Starts threaded handler on file"""
	subprocess.call('python '+str(file), shell=False)
	update_console('starting handler...')

def handle():
	"""Starts idle handler"""
	thread = Thread(target = threader, args = ('python_remote_handler.py', ))
	thread.start()

def execute(command, arg1=None, arg2=None, arg3=None):
	"""Runs a custom command"""
	if arg1!=None and arg2!=None and arg3!=None:
		methodToCall = getattr(master_lib, command)(arg1,arg2,arg3)
		response = methodToCall(arg1,arg2,arg3)
	elif arg1!=None and arg2!=None:
		methodToCall = getattr(master_lib, command)(arg1,arg2)
		response = methodToCall(arg1,arg2)
	elif arg1!=None:
		methodToCall = getattr(master_lib, command)(arg1)
		response = methodToCall(arg1)
	else:
		methodToCall = getattr(master_lib, command)
		response = methodToCall()

def debug():
	"""Enables or Disables debug mode
	debug mode will catch errors but it will stop execution of commands when found"""
	if __builtin__.debug==0:
		__builtin__.debug=1
		update_console('debug state is now ON')
	elif __builtin__.debug==1:
		__builtin__.debug=0
		update_console('debug state is now OFF')
