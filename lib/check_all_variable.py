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
result = GF.check_all_variable(sys.argv[1])
print result

