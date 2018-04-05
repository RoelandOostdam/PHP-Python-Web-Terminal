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
	print 'Connected to db'

def close():
	global db,cur
	db.close()

def waitForInput(interval):
	global db,cur
	interval = interval/1000
	while True:
		sendUpdate()
		cur.execute("SELECT * FROM terminal_feed ORDER BY datetime DESC LIMIT 1")

		if(cur.rowcount!=0):
			record = cur.fetchall()[0]
			record_id = record[0]
			record_thread = record[1]
			record_datetime = record[2]
			record_feed = record[3]

			if record_datetime > datetime.datetime.now()-datetime.timedelta(seconds=interval+interval*0.5):
				#print "found: "+str(record_feed)[:7]
				if(record_feed[:8]=='##input:'):
					command = record_feed[8:]
					print 'Executing: '+ command
					try:
						eval(command)()
					except Exception as e:
						print 'Error in function: '+str(e)
						addFeed(0,'Error in function: '+str(e))
		time.sleep(interval)

def retrieveAll(selection):
	global db,cur
	cur.execute("SELECT "+selection+" FROM terminal_feed")
	for row in cur.fetchall():
		return row

def addFeed(thread_id=0,feed='Empty feed'):
	global db,cur
	try:
		cur.execute("INSERT INTO terminal_feed (thread_id, feed) VALUES ('"+str(thread_id)+"', '"+str(feed)+"')")
	except Exception as e:
		cur.execute("INSERT INTO terminal_feed (thread_id, feed) VALUES ('0','An SQL error occured')")
	db.commit()

def sendUpdate(thread=0,response='Response'):
	global db,cur
	print 'Sending ping'
	cur.execute("SELECT * FROM terminal_threads WHERE thread=0")
	if(cur.rowcount!=0):
		cur.execute("UPDATE terminal_threads SET status = '"+str(response)+"', status_datetime=CURRENT_TIMESTAMP() WHERE thread="+str(thread))
		db.commit()
	else:
		cur.execute("INSERT INTO terminal_threads (thread, status) VALUES (0,'response')")
		db.commit()

def cls():
	global db,cur
	cur.execute("TRUNCATE TABLE terminal_feed")
	db.commit()

def test():
	global db,cur
	addFeed(0,'test')