#Required core & scope execute
import core
def execute(command):
	eval(command)

#Core response functions:
# core.addFeed(feed='Empty feed',thread_id=0)    -- Sends a new feed to the terminal
# core.sendUpdate(response='Response',thread=0)	-- Sends a new update status/ping to the thread

#Custom user libary functions

def test():
	core.addFeed('test',0)