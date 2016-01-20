#/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse,os,git,subprocess,sys
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

# 更新code
parser.add_argument("-u", "--update", help="update graphwalker source code")
# Merge all graph
parser.add_argument("-m", "--model", help="merge graph ,please input graph folder") 
# Check graphical integrity
parser.add_argument("-c", "--check", help="Check graphical integrity",action="store_true") 
# Running graphwalker
parser.add_argument("-r", "--run", help="running graphwalker",action="store_true") 
# Screenshot
parser.add_argument("-s", "--shot", help="Screenshot when error occured, input pc or mobile") 
# Stop Condition
parser.add_argument("-S", "--Stop", help="Set stop condition",default="random(edge_coverage(100))") 


# 解析參數
args = parser.parse_args()

#get current location
current_locate = os.popen('pwd').read().strip('\n')

#creat folder [init]
if not os.path.exists('/usr/local/GraphwalkerRunner'):
	# git clone code
	print 'git clone code...'
	# git.Git().clone("git://github.com/jeremy016/GraphwalkerRunner.git")
	print os.popen('sudo git clone https://github.com/jeremy016/GraphwalkerRunner').read()
	
	print 'creat tool folder'
	os.popen('sudo mv -f GraphwalkerRunner /usr/local/GraphwalkerRunner')

	#download graphwalker-cli-3.4.0-SNAPSHOT.jar

	print 'download graphwalker-cli-SNAPSHOT.jar'
	req = urllib2.Request('https://justup.co/api/v1.1/download/files',headers = {"Content-Type":"application/json"},data = '{"filelist":[{"fileid":"c84d674b-c645-4a2b-a5f0-8afd931b005e","password":""}]}')
	req.get_method = lambda: 'POST'
	Request_detail = json.loads(urllib2.urlopen(req).read())
	print os.popen('sudo wget --no-check-certificate "'+Request_detail['downloadURL']+'" -O /usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar').read()

	#改權限
	os.popen('sudo chmod -R 777 /usr/local/GraphwalkerRunner')


#merge graph [-m]
if args.model:
	print 'merge graph...'
	#merge graph (graph_merge.py)
	command = 'python /usr/local/GraphwalkerRunner/lib/graph_merge.py '+args.model+' '+current_locate
	os.popen(command)

	#graphml -> dot
	print 'graphml -> dot... (merged.dot)'
	command = 'java -jar /usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar convert -i '+current_locate+'/merged.graphml '+current_locate+'/merged.dot'
	os.popen(command)

	#dot -> png  , apt-get install graphviz
	print 'dot -> png... (merged.png)'
	command = 'dot -Tpng '+current_locate+'/merged.dot > '+current_locate+'/merged.png'
	os.popen(command)

	#output merged.py
	command = 'java -jar /usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar source -i '+current_locate+'/merged.graphml /usr/local/GraphwalkerRunner/lib/python.template > '+current_locate+'/merged.py'
	os.popen(command)

	#stripping function
	print 'Generate python stub source code & graphwalker Runner ... (script.py)'
	command = 'python /usr/local/GraphwalkerRunner/lib/stripping.py '+current_locate
	os.popen(command)

	#del dot
	command = 'rm '+current_locate+'/merged.dot '+current_locate+'/merged.py'
	os.popen(command)
	
#Check graphical integrity [-c]
if args.check:
	print 'Check graphical integrity'
	command = 'python /usr/local/GraphwalkerRunner/lib/check_graphical_integrity.py '+current_locate
	result = os.popen(command).read()

#running graphwalker [-r]
if args.run:
	print 'graphwalker running'
	#copy script to tool
	command = 'cp '+current_locate+'/script.py /usr/local/GraphwalkerRunner/lib/script.py'
	os.popen(command)
	
	#Stop Condition [-S]
	args.Stop = args.Stop.replace('(','\\(').replace(')','\\)')
	command = 'python /usr/local/GraphwalkerRunner/lib/Runner.py '+current_locate+' '+args.Stop

	#Screenshot [-s]
	if args.shot:
		command += ' '+args.shot
	
	#Running GraphwalkerRunner
	p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
	output_immediately()
	
