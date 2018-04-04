import MySQLdb
import time, datetime, os

global db,cur

def connect(host,user,passwd):
	global db,cur
	db = MySQLdb.connect(
		host=host,
		user=user,
		passwd=passwd,
		db="terminal_data")
	cur = db.cursor()

def close():
	global db,cur
	db.close()

def waitForInput():
	global db,cur
	#while True:
	print 'waiting for command..'
	cur.execute("SELECT * FROM terminal_feed ORDER BY datetime DESC LIMIT 1")

	record = cur.fetchall()[0]
	record_id = record[0]
	record_thread = record[1]
	record_datetime = record[2]
	record_feed = record[3]

	if record_datetime > datetime.datetime.now()-datetime.timedelta(seconds=2000000000):
		#print "found: "+str(record_feed)[:7]
		if(record_feed[:8]=='##input:'):
			command = record_feed[8:]
			print 'command found: '+ command
			try:
				eval(command)()
			except Exception as e:
				print 'Error in function: '+str(e)
	#time.sleep(1)

def retrieveAll(selection):
	global db,cur
	cur.execute("SELECT "+selection+" FROM terminal_feed")
	for row in cur.fetchall():
		return row

def addFeed(thread_id,feed):
	global db,cur
	cur.execute("INSERT INTO terminal_feed ("+thread_id+", "+feed+") VALUES ()")

def test():
	print 'test output'