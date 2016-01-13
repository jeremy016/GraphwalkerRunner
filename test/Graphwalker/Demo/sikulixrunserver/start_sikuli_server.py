#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import urllib2, os, sys, time

#start sikuli server
def start_sikuli_server():
	try:
		#os.popen("kill $(ps aux | grep 'java -jar " + SIKULI_JAR + "' | grep -v grep | awk '{print $2}')")
		os.popen('java -jar ' + SIKULI_JAR + ' -s &')
		time.sleep(5)
		print 'start server...'
	except Exception as e:
		print 'Start Sikuli Server Error: ' + str(e)
		exit()

def set_sikuli_script_home():
	try:
		urllib2.urlopen('http://localhost:50001/scripts' + SIKULI_SCRIPT_PATH)
		print 'set script home...'
	except Exception as e:
		print 'Set Sikuli Home Error: ' + str(e)
		exit()

#/home/tonychang/sikulixrunserver/
SIKULI_JAR = sys.argv[1]
SIKULI_SCRIPT_PATH = sys.argv[2]

start_sikuli_server()
set_sikuli_script_home()
