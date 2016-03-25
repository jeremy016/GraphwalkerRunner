# -*- coding: utf-8 -*-
import sys
sys.path.append(sys.argv[2])
import script as Script

import logging
import logging.config

reload(sys)  
sys.setdefaultencoding('utf8')

##########Set log################

logging.config.fileConfig("/usr/local/GraphwalkerRunner/logger.conf")
logger = logging.getLogger("example01")

#################################


def main():
	argv_1 = sys.argv[1]
	rundown = argv_1.split('->')

	try:
		for point in rundown:

			logger.debug(eval( "Script."+point + "()" ))

	except:
		error_type, message, traceback = sys.exc_info()

		logger.error('error type : '+str(error_type))
		logger.error('error msg : '+str(message))
		logger.error('function or module : '+ str(point))
		logger.error('file : '+ str(traceback.tb_frame.f_code.co_filename))
	        

		

if __name__ == "__main__":
    main()

 