from core.core import *

try:
	with open('config.cfg') as f:
	    content = f.readlines()
	content = [x.strip() for x in content] 
	host = content[0][5:]
	user = content[1][5:]
	passwd = content[2][7:]
	interval = content[3][9:]
	queue_limit = content[4][12:]
except Exception as e:
	print 'Error reading config: '+str(e)

init(host,user,passwd,1,queue_limit)

#close()