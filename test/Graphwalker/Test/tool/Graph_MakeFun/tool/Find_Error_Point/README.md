Find_Error_Point
===========

This module will assist in finding problem point


How to Run
===========
1. merge graphml & output executable file and function name text & Run websocket
    
    $ bash Run.sh <grapg folder>
    
    Output message:
	    merge graphml...$1




		graphml -> dot... (merged.dot)
		please install graphviz
		dot -> png... (merged.png)
		Generate python stub source code... (merged.py)
		Gwebsocket Running...
		十二月 18, 2015 1:42:06 下午 com.sun.jersey.server.impl.application.WebApplicationImpl _initiate
		資訊: Initiating Jersey application, version 'Jersey: 1.18.3 12/01/2014 08:23 AM'
		十二月 18, 2015 1:42:06 下午 org.glassfish.grizzly.http.server.NetworkListener start
		資訊: Started listener bound to [0.0.0.0:8887]
		十二月 18, 2015 1:42:06 下午 org.glassfish.grizzly.http.server.HttpServer start
		資訊: [HttpServer] Started.
		Try http://localhost:8887/graphwalker/hasNext or http://localhost:8887/graphwalker/getNext
		Press Control+C to end...
  
2. open other terminal & Run executable file: 
	
	$ python merged.py	

	Output message:
		list length : 62

		==============================
		count = length * length 
		==============================

		Spend time:14.3357820511

		error point : 
		['v_Login_PrivacyPolicyPage']
