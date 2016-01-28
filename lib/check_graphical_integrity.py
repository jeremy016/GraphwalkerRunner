# -*- coding: utf-8 -*-
import sys
import GraphFun as GraphFun
import logging
import logging.config

#creat GraphFun object----------------


##########Set log################

logging.config.fileConfig("/usr/local/GraphwalkerRunner/logger.conf")
logger = logging.getLogger("example01")

#################################


GF = GraphFun.GraphFun()

try:
	result = GF.timeout('CheckGraphicalIntegrity',sys.argv[1])
	assert result==True,'Graphics incomplete'

except Exception as error:
	logger.error(str(error))

