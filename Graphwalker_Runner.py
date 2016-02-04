#/usr/bin/env python
# -*- coding: utf-8 -*-

import os,subprocess,sys,json,shlex
import logging,argparse,urllib2
import logging.config

from subprocess import Popen, PIPE


runner_version='1.0.0'
# logger setting

try:
	logging.config.fileConfig("/usr/local/GraphwalkerRunner/logger.conf")

except Exception :

	print 'git clone code...'
	os.popen('sudo git clone https://github.com/jeremy016/GraphwalkerRunner').read()
	
	print 'creat tool folder'
	os.popen('sudo mv -f GraphwalkerRunner /usr/local/GraphwalkerRunner').read()

	print 'get ".jar" downloadURL...'
	req = urllib2.Request('https://justup.co/api/v1.1/download/files',headers = {"Content-Type":"application/json"},data = '{"filelist":[{"fileid":"c84d674b-c645-4a2b-a5f0-8afd931b005e","password":""}]}')
	req.get_method = lambda: 'POST'
	Request_detail = json.loads(urllib2.urlopen(req).read())

	print 'Download graphwalker-cli-SNAPSHOT.jar...'
	os.popen('sudo wget --no-check-certificate '+Request_detail['downloadURL']+' -O /usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar').read()	

	print 'get "Runner" downloadURL...'
	req = urllib2.Request('https://justup.co/api/v1.1/download/files',headers = {"Content-Type":"application/json"},data = '{"filelist":[{"fileid":"cc9139b0-8094-4ba0-8d03-72dc6e483ff4","password":""}]}')
	req.get_method = lambda: 'POST'
	Request_detail = json.loads(urllib2.urlopen(req).read())

	print 'Download Runner...'
	os.popen('sudo wget --no-check-certificate '+Request_detail['downloadURL'] +' -O /usr/bin/Graphwalker_Runner').read()	
	
	print 'chmod folder...'
	os.popen('sudo chmod -R 777 /usr/local/GraphwalkerRunner').read()	


logger = logging.getLogger("example01")

def call(command,output_file=''):
	p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
	output, error = p.communicate()
	if p.returncode == 0:
		if output:
			if output_file:
				with open(output_file, 'w') as outfile:
				    outfile.write(str(output))
			else:
				logger.info(output)
		else:
			logger.info('successful')
	else:
	   	logger.error(str(error))

def output_immediately():
	while True:
	    out = p.stderr.read(1)
	    if out == '' and p.poll() != None:
	        break
	    if out != '':
	        sys.stdout.write(out)
	        sys.stdout.flush()

	    

# 建立一個參數解析器，並為程式功能加上說明
parser = argparse.ArgumentParser(description='Graphwalker Runner')


# init
parser.add_argument("-i", "--init", help="Rebuild graphwalker environment , syntax：Graphwalker_Runner -i ",action="store_true") 
# 更新code
parser.add_argument("-u", "--update", help="Pull graphwalker source code from github, syntax：Graphwalker_Runner -u ",action="store_true")
# Merge all graph
parser.add_argument("-m", "--model", help="Merge graphml files in folder ,folderpattern: graphml folder path, syntax：Graphwalker_Runner -m <folderpattern>") 
# Check graphical integrity
parser.add_argument("-c", "--check", help="Check graphical integrity, output Not visited points file (Not_visited_points.txt) ,syntax：Graphwalker_Runner -c ",action="store_true") 
# Running graphwalker
parser.add_argument("-r", "--run", help="Running graphwalker, syntax：Graphwalker_Runner -r",action="store_true") 
# Screenshot
parser.add_argument("-s", "--shot", help="Screenshot when graphwalker running, TestDevice: 'pc' or 'mobile' , syntax: Graphwalker_Runner -r -s <TestDevice>") 
# Stop Condition
parser.add_argument("-S", "--Stop", help="Set stop condition, default StopCondition: 'random(edge_coverage(100))' , syntax: Graphwalker_Runner -r -S <StopCondition>",default="random(edge_coverage(100))") 
# Version
parser.add_argument("-v", "--version", help="Show current version number and change notes",action="store_true")
# All Version
parser.add_argument("-vv", "--ChangeNotes", help="Show all version number and change notes ",action="store_true")


# 解析參數
args = parser.parse_args()

#get current location
current_locate = os.popen('pwd').read().strip('\n')

# show version
if args.version:
	
	try:

		with open('/usr/local/GraphwalkerRunner/version.json') as f:
			contents = json.loads(f.read())
			print '\n Current Version:',contents['tool']['latest']['Version']
			print ' Change log：'
			for i in contents['tool']['latest']['Change log']:
				print '   ',contents['tool']['latest']['Change log'].index(i)+1,'：',i.encode('utf-8')
			if runner_version != contents['runner']['latest']['Version']:
				print '\n****************** Warning ********************'
				print '\n Runner has new version : '+str(contents['runner']['latest']['Version'])
				print '\n please update by runner_update (Ubuntu executable) '
				print '\n "runner_update" download URL : https://justup.co/share.html?id=88fab911-0ee0-4614-8702-f30b812487cf'
				print '\n***********************************************'

	except Exception,e:

		logger.error(str(e))

# show ChangeNotes
if args.ChangeNotes:
	
	try:

		with open('/usr/local/GraphwalkerRunner/version.json') as f:
			contents = json.loads(f.read())

			print '\n Current Version:',contents['tool']['latest']['Version']
			print ' Change log：'
			for i in contents['tool']['latest']['Change log']:
				print '   ',contents['tool']['latest']['Change log'].index(i)+1,'：',i.encode('utf-8')
		
			for i in contents['tool']['old']:
				print '\n Version:',i['Version']
				print ' Change log：'
				for ii in i['Change log']:
					print '   ',i['Change log'].index(ii)+1,'：',ii.encode('utf-8')
			
	except Exception,e:

		logger.error(str(e))



#init environment [-i]
if args.init:
	
	if os.path.exists('/usr/local/GraphwalkerRunner'):

		call(['sudo','rm','-rf','/usr/local/GraphwalkerRunner'])

	print 'git clone code...'
	os.popen('sudo git clone https://github.com/jeremy016/GraphwalkerRunner').read()
	
	print 'creat tool folder'
	os.popen('sudo mv -f GraphwalkerRunner /usr/local/GraphwalkerRunner').read()

	print 'get ".jar" downloadURL...'
	req = urllib2.Request('https://justup.co/api/v1.1/download/files',headers = {"Content-Type":"application/json"},data = '{"filelist":[{"fileid":"c84d674b-c645-4a2b-a5f0-8afd931b005e","password":""}]}')
	req.get_method = lambda: 'POST'
	Request_detail = json.loads(urllib2.urlopen(req).read())

	print 'Download graphwalker-cli-SNAPSHOT.jar...'
	os.popen('sudo wget --no-check-certificate '+Request_detail['downloadURL']+' -O /usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar').read()	

	# print 'get "Runner" downloadURL...'
	# req = urllib2.Request('https://justup.co/api/v1.1/download/files',headers = {"Content-Type":"application/json"},data = '{"filelist":[{"fileid":"cc9139b0-8094-4ba0-8d03-72dc6e483ff4","password":""}]}')
	# req.get_method = lambda: 'POST'
	# Request_detail = json.loads(urllib2.urlopen(req).read())

	# print 'Download Runner...'
	# os.popen('sudo wget --no-check-certificate '+Request_detail['downloadURL'] +' -O /usr/bin/Graphwalker_Runner').read()	
	
	print 'chmod folder...'
	os.popen('sudo chmod -R 777 /usr/local/GraphwalkerRunner').read()	

	
#更新code
if args.update:

	# git pull date
	# print 'update...'
	logger.info('update...')
	call(['bash','/usr/local/GraphwalkerRunner/lib/git_pull.sh'])
	
	# try:
	# 	logger.info('get "Runner" downloadURL...')
	# 	req = urllib2.Request('https://justup.co/api/v1.1/download/files',headers = {"Content-Type":"application/json"},data = '{"filelist":[{"fileid":"cc9139b0-8094-4ba0-8d03-72dc6e483ff4","password":""}]}')
	# 	req.get_method = lambda: 'POST'
	# 	Request_detail = json.loads(urllib2.urlopen(req).read())

	# except Exception,e:
	# 	logger.error(str(e))

	# logger.info('Download Runner...')
	# call(['sudo','wget','--no-check-certificate',Request_detail['downloadURL'],'-O','/usr/bin/Graphwalker_Runner'])

	# #改權限
	# logger.info('chmod folder...')
	# call(['sudo','chmod','-R','777','/usr/local/GraphwalkerRunner'])
	
#merge graph [-m]
if args.model:

	try:

		logger.info('merge graph...')
		call(['python','/usr/local/GraphwalkerRunner/lib/graph_merge.py',args.model,current_locate])

		
		#graphml -> dot
		logger.info('graphml -> dot... (merged.dot)')
		call(['java','-jar','/usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar','convert','-i',current_locate+'/merged.graphml',current_locate+'/merged.dot'])		

		
		#dot -> png  , apt-get install graphviz
		logger.info('dot -> png... (merged.png)')
		call(['dot','-Tpng',current_locate+'/merged.dot','-o',current_locate+'/merged.png'])


		
		#output merged.py
		logger.info('output merged.py')
		call(['java','-jar','/usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar','source','-i',current_locate+'/merged.graphml','/usr/local/GraphwalkerRunner/lib/python.template'],current_locate+'/merged.py')
		

		#stripping function
		logger.info('Generate python stub source code & graphwalker Runner ... (script.py)')
		call(['python', '/usr/local/GraphwalkerRunner/lib/stripping.py',current_locate])

		#del dot
		logger.info('del dot')
		call(['rm',current_locate+'/merged.dot',current_locate+'/merged.py'])
	

	except Exception,e:
		logger.error(str(e))

#Check graphical integrity [-c]
if args.check:

	logger.info('Check graphical integrity')
	os.popen('python /usr/local/GraphwalkerRunner/lib/check_graphical_integrity.py '+ current_locate).read()
	#call(['python','/usr/local/GraphwalkerRunner/lib/check_graphical_integrity.py',current_locate])

#running graphwalker [-r]
if args.run:

	logger.info('graphwalker running')

	try:
		
		#copy script to tool
		call(['cp',current_locate+'/script.py','/usr/local/GraphwalkerRunner/lib/script.py'])

		
		#Stop Condition [-S]
		args.Stop = args.Stop.replace('(','\\(').replace(')','\\)')
		command = 'python /usr/local/GraphwalkerRunner/lib/Runner.py '+current_locate+' '+str(args.Stop)

		
		#Screenshot [-s]
		if args.shot:
			command += ' '+args.shot
		
		#Running GraphwalkerRunner
		p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
		output_immediately()

	
	except Exception, e:

		logger.error(str(e))
