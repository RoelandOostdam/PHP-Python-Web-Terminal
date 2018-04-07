import MySQLdb
import time, datetime, os, sys
from threading import Thread
#Custom libs
import custom_lib
#Core functions
core_fncs = ['cls','flush','cflush']

def init(host,user,passwd,p_interval,p_queue_limit):
	global p_host, p_user, p_passwd, interval, queue_limit
	p_host = host
	p_user = user
	p_passwd = passwd
	interval = int(p_interval)
	queue_limit = int(p_queue_limit)

	connect(host,user,passwd)
	waitForInput()

def connect(host,user,passwd):
	global db,cur
	db = MySQLdb.connect(
		host=p_host,
		user=p_user,
		passwd=p_passwd,
		db="terminal_data")
	cur = db.cursor()
	#print 'Connected to db'

def close():
	db.close()

def reconnect():
	try:
		db.close()
		connect(p_host,p_user,p_passwd)
	except:
		pass

def waitForInput():
	commands = []
	while True:
		reconnect()
		sendUpdate()
		try:
			cur.execute("SELECT * FROM terminal_feed ORDER BY datetime DESC LIMIT "+str(queue_limit))
		except Exception as e:
			print "MySQL could not queue command (#1001): "+str(e)
			pass

		if(cur.rowcount!=0):
			for record in cur.fetchall():
				record_id = record[0]
				record_thread = record[1]
				record_datetime = record[2]
				record_feed = record[3]

				if record_datetime > datetime.datetime.now()-datetime.timedelta(seconds=(interval*2)+queue_limit+2):
					#print "found: "+str(record_feed)[:7]
					if(record_feed[:8]=='##input:'):
						command = record_feed[8:]
						if(record_id not in commands):
							print 'Executing: '+ command
							try:
								commands.append(record_id)
								if(command in core_fncs):
									eval(command)()
								else:
									if '(' in command:
										cur.execute("SELECT MAX(thread) FROM terminal_threads")
										thread_assign = int(cur.fetchall()[0][0])+1
										print 'Assigning thread: '+str(thread_assign)+' running command: '+str(command)
										thread = Thread(target = custom_lib.execute, args = (command,thread_assign))
										thread.start()
										#thread.join()
										#custom_lib.execute(command)
									else:
										addFeed(command+' is not a function. Call a function with ()')
							except Exception as e:
								print 'Error in function: '+str(e)
								addFeed('Error in function: '+str(e))
							print 'Next in queue'
							time.sleep(0.5)
						else:
							pass
		time.sleep(interval)

def addFeed(feed='Empty feed',thread_id=0):
	try:
		cur.execute("INSERT INTO terminal_feed (thread_id, feed) VALUES ('"+str(thread_id)+"', '"+str(feed)+"')")
		db.commit()
	except Exception as e:
		try:
			cur.execute("INSERT INTO terminal_feed (thread_id, feed) VALUES ('0','Input error')")
			db.commit()
		except Exception as e:
			print 'MySQL could not queue command (#1002): '+str(e)
	
def sendUpdate(response='Response',thread_id=0):
	print("Ping " + time.strftime("%H:%M:%S", time.gmtime()))
	try:
		cur.execute("SELECT * FROM terminal_threads WHERE thread="+str(thread_id))
		if(cur.rowcount!=0):
			cur.execute("UPDATE terminal_threads SET status = '"+str(response)+"', status_datetime=CURRENT_TIMESTAMP() WHERE thread="+str(thread_id))
			db.commit()
		else:
			cur.execute("INSERT INTO terminal_threads (thread, status) VALUES ("+str(thread_id)+",'"+str(response)+"')")
			db.commit()
	except Exception as e:
		try:
			cur.execute("INSERT INTO terminal_feed (thread_id, feed) VALUES ('0','MySQL could not queue command')")
		except Exception as e:
			print 'MySQL could not queue command (#1003): '+str(e)

def completeTask(thread_id=0):
	sendUpdate('##c:Task completed',thread_id)
	time.sleep(5)
	try:
		cur.execute("DELETE FROM terminal_threads WHERE thread="+str(thread_id))
		db.commit()
	except Exception as e:
			print 'MySQL could not queue command (#1004): '+str(e)

def cls():
	cur.execute("TRUNCATE TABLE terminal_feed")
	db.commit()

def flush():
	cur.execute("TRUNCATE TABLE terminal_threads")
	addFeed('Threads flushed')
	db.commit()

def cflush():
	cls()
	flush()

