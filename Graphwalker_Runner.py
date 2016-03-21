#/usr/bin/env python
# -*- coding: utf-8 -*-

import os,subprocess,sys,json,shlex,re
import logging,argparse,urllib2
import logging.config

sys.path.append('/usr/local/GraphwalkerRunner')

from lib.Set_Resource import *
# from lib.check_graphical_integrity import *
from subprocess import Popen, PIPE


runner_version='1.0.9'
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

	print 'Download Graphwalker_Runner...'
	os.popen('sudo wget --no-check-certificate '+Request_detail['downloadURL'] +' -O /usr/bin/Graphwalker_Runner').read()	
	
	print 'chmod folder...'
	os.popen('sudo chmod -R 775 /usr/local/GraphwalkerRunner').read()

	print 'chmod Runner...'
	os.popen('sudo chmod -R 775 /usr/bin/Graphwalker_Runner').read()




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
			if error:
				logger.info(error)
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
parser.add_argument("-c", "--check", help="Check graphical integrity, output Not visited points file (Not_visited_points.txt),timeout: nput timeout second ,syntax：Graphwalker_Runner -c 'timeout'") 
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
# Visits specific path
parser.add_argument("-p", "--path", help="Visits specific path , syntax: Graphwalker_Runner -p 'path', path syntax : 'point(0)->point(2)->point(3)' ")
# Logcat Saving
parser.add_argument("-l", "--logcat", help="Saving android logcat information , syntax: Graphwalker_Runner -r -l ",action="store_true") 
# Set Devices 
parser.add_argument("-d", "--devices", help="Setting mobile devices , syntax: Graphwalker_Runner -r -d 'devices number' or 'list' , input 'list' can select ") 


# 解析參數
args = parser.parse_args()

#get current location
current_locate = os.popen('pwd').read().strip('\n')

# show version
if args.version:
	
	try:

		with open('/usr/local/GraphwalkerRunner/version.json') as f:
			contents = json.loads(f.read())

			print '\n****************** Current Versions ********************'
			print '\nCurrent Runner Version:',str(runner_version)
			print '\nCurrent Tool Version:',contents['tool']['latest']['Version']
			print 'Change log：'
			for i in contents['tool']['latest']['Change log']:
				print '   ',contents['tool']['latest']['Change log'].index(i)+1,'：',i.encode('utf-8')
			if runner_version != contents['runner']['latest']['Version']:
				print '\n****************** Warning ********************'
				print '\n Runner has new version : '+str(contents['runner']['latest']['Version'])
				print ' Change log：'
				for i in contents['runner']['latest']['Change log']:
					print '   ',contents['runner']['latest']['Change log'].index(i)+1,'：',i.encode('utf-8')
				print '\n please update by runner_update (Ubuntu executable) '
				print '\n "runner_update" download URL : https://justup.co/share.html?id=88fab911-0ee0-4614-8702-f30b812487cf'
			print '\n********************************************************'

	except Exception,e:

		logger.error(str(e))

# show ChangeNotes
elif args.ChangeNotes:
	
	try:

		with open('/usr/local/GraphwalkerRunner/version.json') as f:
			contents = json.loads(f.read())

			print '\n****************** Current Versions ********************'
			print '\nCurrent Runner Version:',str(runner_version)
			print '\nCurrent Tool Version:',contents['tool']['latest']['Version']
			print 'Change log：'
			
			for i in contents['tool']['latest']['Change log']:
				print '   ',contents['tool']['latest']['Change log'].index(i)+1,'：',i.encode('utf-8')
			
			print '\n****************** Previous Versions ********************'
			for i in contents['tool']['old']:
				print '\n Version:',i['Version']
				print ' Change log：'
				for ii in i['Change log']:
					print '   ',i['Change log'].index(ii)+1,'：',ii.encode('utf-8')

			if runner_version != contents['runner']['latest']['Version']:
				print '\n********************* Warning ***********************'
				print '\n Runner has new version : '+str(contents['runner']['latest']['Version'])
				print ' Change log：'
				for i in contents['runner']['latest']['Change log']:
					print '   ',contents['runner']['latest']['Change log'].index(i)+1,'：',i.encode('utf-8')
				print '\n please update by runner_update (Ubuntu executable) '
				print '\n "runner_update" download URL : https://justup.co/share.html?id=88fab911-0ee0-4614-8702-f30b812487cf'
			print '\n*********************************************************'
			
	except Exception,e:

		logger.error(str(e))


# Visits specific path
elif args.path:

	try:

		#copy script to tool
		call(['cp',current_locate+'/script.py','/usr/local/GraphwalkerRunner/lib/script.py'])

		#run script by specific path
		logger.info('run script by specific path...')
		print os.popen('python /usr/local/GraphwalkerRunner/lib/Run_Specified_Path.py \''+str(args.path)+'\'').read()



	except Exception,e:

		logger.error(str(e))



#init environment [-i]
elif args.init:
	
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
elif args.update:

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
elif args.model:

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
elif args.check:

	logger.info('Check graphical integrity')

	os.popen('python -W ignore /usr/local/GraphwalkerRunner/lib/check_graphical_integrity.py '+ current_locate+' '+args.check).read()
	# call(['python','/usr/local/GraphwalkerRunner/lib/check_graphical_integrity.py',current_locate,args.check])
	# GF = check_graphical_integrity()
	# timeout=int(args.check)
	# GF.CheckGraphicalIntegrity(current_locate,timeout)

#running graphwalker [-r]
elif args.run:

	logger.info('graphwalker running')

	try:
		
		#copy script to tool
		# call(['cp',current_locate+'/script.py','/usr/local/GraphwalkerRunner/lib/script.py'])


		#Set Devices [-d]
		if args.devices :

			resource = Set_Resource(current_locate)

			# select one
			if args.devices == "list":

				devices_info = os.popen('adb devices').read()
				
				p = re.compile(r'\n(.*)\t')
				
				d_list = p.findall(devices_info)
				
				print 'Devices List:'

				for i in d_list:
					print str(d_list.index(i)+1)+'.  '+str(i)

				get_input = input('Please select one :')
				resource.set_androidDeviceSerial(str(d_list[int(get_input)-1]))
				args_devices = str(d_list[int(get_input)-1])
			# get input 
			else:
				resource.set_androidDeviceSerial(str(args.devices))
				args_devices = args.devices

			
		
		#Stop Condition [-S]
		args.Stop = args.Stop.replace('(','\\(').replace(')','\\)')
		command = 'python /usr/local/GraphwalkerRunner/lib/Runner.py '+current_locate+' '+str(args.Stop) 
		# command = 'python /usr/local/GraphwalkerRunner/lib/Runner.py '+current_locate+' '+str(args.Stop)

		
		#Screenshot [-s]
		if args.shot:
			command += ' '+args.shot
		else:
			command += ' False'


		#logcat [-l]
		if args.logcat:
			command += ' True'
		else:
			command += ' False'

		#Devices [-d]
		if args.devices:
			command += ' '+args_devices
		else:
			command += ' False'
		
		#Running GraphwalkerRunner
		p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
		output_immediately()

	
	except Exception, e:
		print e
		logger.error(str(e))


	




else:
	parser.print_help()

	
	