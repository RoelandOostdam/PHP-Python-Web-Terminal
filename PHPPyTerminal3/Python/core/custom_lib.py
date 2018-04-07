#Required core & scope function
import core
from threading import Thread
def execute(command,pthread):
	global thread
	thread = pthread
	core.sendUpdate("Executing: "+str(command),thread)
	
	try:
		eval(command)
	except Exception as e:
		core.addFeed(str(e),thread)

	thread = Thread(target = core.completeTask, args = (pthread,))
	thread.start()
	#thread.join()

#Core response functions:
# core.addFeed(feed='Empty feed',thread_id=0)    -- Sends a new feed to the terminal
# core.sendUpdate(response='Response',thread=0)	 -- Sends a new update status/ping to the thread
# Use global var 'thread' when creating an update or feed

#Custom user libary functions
import time

def test(): #example function
	core.addFeed('test',thread)
	time.sleep(5)