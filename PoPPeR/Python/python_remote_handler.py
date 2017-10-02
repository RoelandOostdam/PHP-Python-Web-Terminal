## @package python_remote_handler
## \brief Executed by python_master_handler to run threaded functions
"""
python_master_handler is the php web-console listener.
It can start threaded remote_handlers to execute functions like auto backup_db
"""

import subprocess, time, datetime
import MySQLdb, status_handler
import time, datetime, os, sys, random
from master_lib import *

process_name = 'python_remote_handler'

def get_command(thread):
	"""Retrieves command for current thread"""
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
	"""Clears current thread commands"""
	db = master_lib.db_connect()
	cursor = db.cursor()
	cursor.execute("DELETE FROM python_remote_handler WHERE thread='" + str(thread) + "'")
	db.commit()
	cursor.close()

def start(thread):
	"""Executes current thread command"""
	print 'assigned thread: ' + str(thread)
	delay = 5
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
				subprocess.call(["python", str(command) + '.py'])


start(random.randrange(100000, 999999))