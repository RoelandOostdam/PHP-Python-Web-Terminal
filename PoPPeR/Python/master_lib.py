import subprocess, time, datetime, StringIO
import MySQLdb, status_handler
import time, datetime, os, sys, random
import master_lib
from threading import Thread

def db_connect():
	global ip, user, password, dbn, db
	ip = "localhost"
	user = "root"
	password = ""
	dbn = "python_data"

	return MySQLdb.connect(ip,user,password,dbn)

def cls():
	db = db_connect()
	cursor = db.cursor()
	cursor.execute("TRUNCATE python_master_console")
	db.commit()
	cursor.close()

def update_console(line, spec='none'):
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
	version = 'PMH running on master_lib 2.0'
	print version
	update_console(version)

def threader(file):
	subprocess.call('python '+str(file), shell=True)
	update_console('starting handler...')

def handle():
	thread = Thread(target = threader, args = ('python_remote_handler.py', ))
	thread.start()


def execute(command, arg1=None, arg2=None, arg3=None):
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