#Required core & scope function
import core
from threading import Thread
#-------------------------------------------------------------------------------------#
#This function is required in each custom library.
#-------------------------------------------------------------------------------------#
def execute(command,pthread):
	global thread
	thread = pthread
	core.sendUpdate(str(thread)+": Executing: "+str(command),thread)
	try:
		command = command.replace('&quot;',"'")
		eval(command)
	except Exception as e:
		print "Thread error: "+str(e)
		core.addFeed("Thread "+str(thread)+' encountered an error: '+str(e),thread)

	thread = Thread(target = core.completeTask, args = (pthread,))
	thread.start()
	#thread.join()

#-------------------------------------------------------------------------------------#
#Core response functions:
#-------------------------------------------------------------------------------------#
# core.addFeed(feed='Empty feed',thread_id=0)    -- Sends a new feed to the terminal
# core.sendUpdate(response='Response',thread=0)	 -- Sends a new update status/ping to the thread
# Use global var 'thread' when creating an update or feed
#-------------------------------------------------------------------------------------#
#Put your custom user libary functions here
import time, subprocess
#-------------------------------------------------------------------------------------#
#example function that directly executes a python command
def pyExec(command,args=''):
	try:
		output = subprocess.check_output([command, args])
		if(output!=None):
			output = 'Empty response'
		print 'Output = '+str(output)
		core.addFeed(str(output),thread)
	except Exception as e:
		core.addFeed('Error in thread '+str(thread)+' executing '+command+': '+str(e),thread)
#example function that returns a feed
def test(text='test'): 
	core.addFeed(str(text),thread)
	time.sleep(5)