#/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse,os,git,subprocess,sys,urllib2,json
#Need install GitPython


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
parser.add_argument("-i", "--init", help="Init graphwalker environment",action="store_true") 
# 更新code
parser.add_argument("-u", "--update", help="Update graphwalker source code",action="store_true")
# Merge all graph
parser.add_argument("-m", "--model", help="It's will merge graphml files in folder , example:Graphwalker_Runner -m 'folder path'") 
# Check graphical integrity
parser.add_argument("-c", "--check", help="Check graphical integrity, output Not visited points file (Not_visited_points.txt) ",action="store_true") 
# Running graphwalker
parser.add_argument("-r", "--run", help="Running graphwalker",action="store_true") 
# Screenshot
parser.add_argument("-s", "--shot", help="Screenshot when graphwalker running, parameter: 'pc' or 'mobile' , example: Graphwalker_Runner -s pc[mobile]") 
# Stop Condition
parser.add_argument("-S", "--Stop", help="Set stop condition, default parameter: 'random(edge_coverage(100))' , example: Graphwalker_Runner -S 'random(edge_coverage(100))'",default="random(edge_coverage(100))") 
# Version
parser.add_argument("-v", "--version", help="Show version number and change notes , parameter: 'new' (show lastest info) or 'all' (show all version info) , example: Graphwalker_Runner -v new[all]")


# 解析參數
args = parser.parse_args()

#get current location
current_locate = os.popen('pwd').read().strip('\n')

# show version
if args.version:
		
	with open('/usr/local/GraphwalkerRunner/version.json') as f:
		contents = json.loads(f.read())

		
		print '\n Current Version:',contents['latest']['Version']
		print ' Change log：'
		for i in contents['latest']['Change log']:
			print '   ',contents['latest']['Change log'].index(i)+1,'：',i.encode('utf-8')

		if args.version == 'all':

			for i in contents['old']:
				print '\n Version:',i['Version']
				print ' Change log：'
				for ii in i['Change log']:
					print '   ',i['Change log'].index(ii)+1,'：',ii.encode('utf-8')



#init environment [-i]
if args.init:
	if os.path.exists('/usr/local/GraphwalkerRunner'):
		os.popen('sudo rm -rf /usr/local/GraphwalkerRunner')


#creat folder [init]
if not os.path.exists('/usr/local/GraphwalkerRunner'):
	# git clone code
	print 'git clone code...'
	# git.Git().clone("git://github.com/jeremy016/GraphwalkerRunner.git")
	print os.popen('sudo git clone https://github.com/jeremy016/GraphwalkerRunner').read()
	
	print 'creat tool folder'
	print os.popen('sudo mv -f GraphwalkerRunner /usr/local/GraphwalkerRunner').read()

	#download graphwalker-cli-3.4.0-SNAPSHOT.jar

	print 'download graphwalker-cli-SNAPSHOT.jar'
	req = urllib2.Request('https://justup.co/api/v1.1/download/files',headers = {"Content-Type":"application/json"},data = '{"filelist":[{"fileid":"c84d674b-c645-4a2b-a5f0-8afd931b005e","password":""}]}')
	req.get_method = lambda: 'POST'
	Request_detail = json.loads(urllib2.urlopen(req).read())
	print os.popen('sudo wget --no-check-certificate "'+Request_detail['downloadURL']+'" -O /usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar').read()

	req = urllib2.Request('https://justup.co/api/v1.1/download/files',headers = {"Content-Type":"application/json"},data = '{"filelist":[{"fileid":"cc9139b0-8094-4ba0-8d03-72dc6e483ff4","password":""}]}')
	req.get_method = lambda: 'POST'
	Request_detail = json.loads(urllib2.urlopen(req).read())
	print os.popen('sudo wget --no-check-certificate "'+Request_detail['downloadURL']+'" -O /usr/bin/Graphwalker_Runner').read()
	
	#改權限
	print os.popen('sudo chmod -R 777 /usr/local/GraphwalkerRunner').read()

#更新code
if args.update:
	# git pull date
	print 'update...'
	print os.popen('bash /usr/local/GraphwalkerRunner/lib/git_pull.sh').read()

	req = urllib2.Request('https://justup.co/api/v1.1/download/files',headers = {"Content-Type":"application/json"},data = '{"filelist":[{"fileid":"cc9139b0-8094-4ba0-8d03-72dc6e483ff4","password":""}]}')
	req.get_method = lambda: 'POST'
	Request_detail = json.loads(urllib2.urlopen(req).read())
	print os.popen('sudo wget --no-check-certificate "'+Request_detail['downloadURL']+'" -O /usr/bin/Graphwalker_Runner').read()

	#改權限
	print os.popen('sudo chmod -R 777 /usr/bin/Graphwalker_Runner').read()

#merge graph [-m]
if args.model:
	print 'merge graph...'
	#merge graph (graph_merge.py)
	command = 'python /usr/local/GraphwalkerRunner/lib/graph_merge.py '+args.model+' '+current_locate
	print os.popen(command).read()

	#graphml -> dot
	print 'graphml -> dot... (merged.dot)'
	command = 'java -jar /usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar convert -i '+current_locate+'/merged.graphml '+current_locate+'/merged.dot'
	print os.popen(command).read()

	#dot -> png  , apt-get install graphviz
	print 'dot -> png... (merged.png)'
	command = 'dot -Tpng '+current_locate+'/merged.dot > '+current_locate+'/merged.png'
	print os.popen(command).read()

	#output merged.py
	command = 'java -jar /usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar source -i '+current_locate+'/merged.graphml /usr/local/GraphwalkerRunner/lib/python.template > '+current_locate+'/merged.py'
	print os.popen(command).read()

	#stripping function
	print 'Generate python stub source code & graphwalker Runner ... (script.py)'
	command = 'python /usr/local/GraphwalkerRunner/lib/stripping.py '+current_locate
	print os.popen(command).read()

	#del dot
	command = 'rm '+current_locate+'/merged.dot '+current_locate+'/merged.py'
	print os.popen(command).read()
	
#Check graphical integrity [-c]
if args.check:
	print 'Check graphical integrity'
	command = 'python /usr/local/GraphwalkerRunner/lib/check_graphical_integrity.py '+current_locate
	print os.popen(command).read()

#running graphwalker [-r]
if args.run:
	print 'graphwalker running'
	#copy script to tool
	command = 'cp '+current_locate+'/script.py /usr/local/GraphwalkerRunner/lib/script.py'
	print os.popen(command).read()
	
	#Stop Condition [-S]
	args.Stop = args.Stop.replace('(','\\(').replace(')','\\)')
	command = 'python /usr/local/GraphwalkerRunner/lib/Runner.py '+current_locate+' '+args.Stop

	#Screenshot [-s]
	if args.shot:
		command += ' '+args.shot
	
	#Running GraphwalkerRunner
	p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
	output_immediately()

	

