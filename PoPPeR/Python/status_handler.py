#python process status response lib
from datetime import datetime
import MySQLdb
import time, datetime, os, sys
from datetime import timedelta
import master_lib


def update_status(process_name, process_update, process_status='no status available'):
	db = master_lib.db_connect()
	cursor = db.cursor()
	cursor.execute("UPDATE python_data SET process_update='" + process_update + "' WHERE process_name='" + process_name + "'")
	db.commit()
	cursor.execute("UPDATE python_data SET process_status='" + process_status + "' WHERE process_name='" + process_name + "'")
	db.commit()
	# data = cursor.fetchone()
	# print data

def init_status(process_name, process_update, process_status='no status available'):
	db = master_lib.db_connect()
	cursor = db.cursor()
	cursor.execute("INSERT INTO python_data (process_name, process_update, process_status) VALUES ('" + process_name + "','" + process_update + "','" + process_status + "')")
	db.commit()

def smart_status(process_name, process_update, process_status='no status available'):
	db = master_lib.db_connect()
	cursor = db.cursor()
	cursor.execute("SELECT * FROM python_data WHERE process_name='" + process_name + "'")
	data = cursor.fetchone()
	if data != None:
		update_status(process_name, process_update, process_status)
	else:
		init_status(process_name, process_update, process_status)

def clear_status(process_name):
	db = master_lib.db_connect()
	cursor = db.cursor()
	cursor.execute("DELETE FROM python_data WHERE process_name='" + process_name + "'")
	db.commit()
	cursor.close()

def get_status(process_name):
	db = master_lib.db_connect()
	cursor = db.cursor()
	cursor.execute("SELECT process_update FROM python_data WHERE process_name='" + process_name + "'")
	process_update = cursor.fetchone()[0]
	print process_update
	cursor.execute("SELECT process_status FROM python_data WHERE process_name='" + process_name + "'")
	process_status = cursor.fetchone()
	process_update = datetime.datetime.strptime(str(process_update), "%Y-%m-%d %H:%M:%S")
	if process_update > datetime.datetime.now() - datetime.timedelta(minutes=3):
		val = 'Heavily Delayed (<3m)'
		if process_update > datetime.datetime.now() - datetime.timedelta(minutes=2):
			val = 'Delayed (<2m)'
			if process_update > datetime.datetime.now() - datetime.timedelta(minutes=1):
				val = 'Healthy (<1m)'
	else:
		val = 'OFFLINE (>3m)'
	return val
	cursor.close()

def timestamp():
	stamp = time.strftime('%Y-%m-%d %H:%M:%S')
	return stamp

def run_test():
	return 'status_handler imported'

#update_status('test_process', time.strftime('%Y-%m-%d %H:%M:%S'), 'test status')
#init_status('test_process', time.strftime('%Y-%m-%d %H:%M:%S'), 'test status')
#smart_status('test_process', time.strftime('%Y-%m-%d %H:%M:%S'), 'test status')
#print get_status('test_process')
#clear_status('xml_generator_controller')