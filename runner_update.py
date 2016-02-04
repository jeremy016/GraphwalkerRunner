#/usr/bin/env python
# -*- coding: utf-8 -*-

import os,subprocess,sys,json,shlex
import argparse,urllib2

print 'get "Runner" downloadURL...'
req = urllib2.Request('https://justup.co/api/v1.1/download/files',headers = {"Content-Type":"application/json"},data = '{"filelist":[{"fileid":"cc9139b0-8094-4ba0-8d03-72dc6e483ff4","password":""}]}')
req.get_method = lambda: 'POST'
Request_detail = json.loads(urllib2.urlopen(req).read())

print 'Download Runner...'
os.popen('sudo wget --no-check-certificate '+Request_detail['downloadURL'] +' -O /usr/bin/Graphwalker_Runner').read()	