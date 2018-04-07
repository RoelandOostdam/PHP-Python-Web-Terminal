import MySQLdb
import time, datetime, os, sys
#Custom libs
import custom_lib
#Core functions
core_fncs = ['cls()']

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
	queue_limit = 10
	interval = interval/1000.0
	commands = []
	while True:
		sendUpdate()
		cur.execute("SELECT * FROM terminal_feed ORDER BY datetime DESC LIMIT "+str(queue_limit))

		if(cur.rowcount!=0):
			for record in cur.fetchall():
				#record = cur.fetchall()[0]
				record_id = record[0]
				record_thread = record[1]
				record_datetime = record[2]
				record_feed = record[3]

				if record_datetime > datetime.datetime.now()-datetime.timedelta(seconds=(interval*2)+1):
					#print "found: "+str(record_feed)[:7]
					if(record_feed[:8]=='##input:'):
						command = record_feed[8:]
						if(record_id not in commands):
							print 'Executing: '+ command
							try:
								commands.append(record_id)
								if(command in core_fncs):
									eval(command)
								else:
									custom_lib.execute(command)
							except Exception as e:
								print 'Error in function: '+str(e)
								addFeed('Error in function: '+str(e),0)
						else:
							#print 'Finished queue'
							pass
		time.sleep(interval)

def addFeed(feed='Empty feed',thread_id=0):
	global db,cur
	try:
		cur.execute("INSERT INTO terminal_feed (thread_id, feed) VALUES ('"+str(thread_id)+"', '"+str(feed)+"')")
	except Exception as e:
		cur.execute("INSERT INTO terminal_feed (thread_id, feed) VALUES ('0','Input error')")
	db.commit()

def sendUpdate(response='Response',thread_id=0):
	global db,cur
	print("Ping " + time.strftime("%H:%M:%S", time.gmtime()))
	cur.execute("SELECT * FROM terminal_threads WHERE thread=0")
	if(cur.rowcount!=0):
		cur.execute("UPDATE terminal_threads SET status = '"+str(response)+"', status_datetime=CURRENT_TIMESTAMP() WHERE thread="+str(thread_id))
		db.commit()
	else:
		cur.execute("INSERT INTO terminal_threads (thread, status) VALUES ("+str(thread_id)+",'response')")
		db.commit()

def cls():
	global db,cur
	cur.execute("TRUNCATE TABLE terminal_feed")
	db.commit()

