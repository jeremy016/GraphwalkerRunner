# -*- coding: utf-8 -*-
import sys
import GraphFun as GraphFun


#creat GraphFun object----------------

GF = GraphFun.GraphFun()

result = GF.timeout('CheckGraphicalIntegrity',sys.argv[1])
assert result==True,'Graphics incomplete'


