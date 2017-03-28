import subprocess, time, datetime
import MySQLdb, status_handler
import time, datetime, os, sys, random
import master_lib
from master_lib import *

process_name = 'python_master_handler'

def get_command(thread):
	db = master_lib.db_connect()
	cursor = db.cursor()
	cursor.execute("SELECT process_name FROM python_remote_handler WHERE thread='" + str(thread) + "'")
	try:
		process_update = cursor.fetchone()[0]
		return process_update
	except:
		return false
	cursor.close()
	
	
def clear_commands(thread):
	db = master_lib.db_connect()
	cursor = db.cursor()
	cursor.execute("DELETE FROM python_remote_handler WHERE thread='" + str(thread) + "'")
	db.commit()
	cursor.close()


def start(thread):
	print 'assigned thread: ' + str(thread)
	delay = 1
	wait = delay
	while True:
		command = None
		status_handler.smart_status(process_name + ' ' + str(thread), status_handler.timestamp(), 'waiting for command: ' + str(wait))
		print 'waiting: ' + str(wait)
		time.sleep(1)
		wait-=1
		if wait<=0:
			wait = delay
			try:
				command = get_command(thread)
				print command
			except:
				command = None
			if command != None:
				clear_commands(thread)
				status_handler.smart_status(process_name + ' ' +  str(thread), status_handler.timestamp(), 'executing: ' + str(command))
				# try:
				command_array = command.split()
				command_array.append(None)
				command_array.append(None)
				command_array.append(None)
				master_lib.update_console(str(command),'y')
				master_lib.execute(command_array[0], command_array[1], command_array[2], command_array[3])
				# 	print 'executing: ' + str(command)
				# except:
				# 	print 'Unknown critical error occured...'


master_lib.update_console('PYTHON_MASTER_HANDLER running ')
start(0)