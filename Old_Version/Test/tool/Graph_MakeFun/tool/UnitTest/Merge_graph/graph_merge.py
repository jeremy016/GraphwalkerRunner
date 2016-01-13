# -*- coding: utf-8 -*- 
import json,os,sys
import xml.etree.ElementTree as ET

from xml.etree.ElementTree import ElementTree
from pygraphml import Graph
from pygraphml import GraphMLParser
import GraphFun 


Complete_graph_path = 'graph/Complete/'
Portion_graph_path = 'graph/Portion/'


#######Complete graph############

#creat GraphFun object
GF = GraphFun.GraphFun()

#read graphml file

all_graph = os.listdir(Complete_graph_path)

merge_grapg = GF.multi_grapg_merge(all_graph,Complete_graph_path)

#graphml_generate
GF.graphml_generate(merge_grapg[0], merge_grapg[1], 'Complete.graphml', debug_flag=False)


#######Complete graph############

#creat GraphFun object
GF = GraphFun.GraphFun()

#read graphml file

all_graph = os.listdir(Portion_graph_path)

merge_grapg = GF.multi_grapg_merge(all_graph,Portion_graph_path)

#graphml_generate
GF.graphml_generate(merge_grapg[0], merge_grapg[1], 'Portion.graphml', debug_flag=False)


#######Compare#########
Complete_list=[]
Complete_dic ={}
Portion_list=[]
Portion_dic = {}

CompleteML = GF.read_graphml('./','Complete.graphml')
for i in CompleteML:
	for ii in i:
		if len(ii) == 2:
			Complete_dic[ii[0]]=ii[1]

		if len(ii) == 4:
			ii[2] = Complete_dic[ii[2]]
			ii[3] = Complete_dic[ii[3]]
			ii.remove(ii[0])
			Complete_list.append(str(ii))

PortionML = GF.read_graphml('./','Portion.graphml')
for i in PortionML:
	for ii in i:
		if len(ii) == 2:
			Portion_dic[ii[0]]=ii[1]

		if len(ii) == 4:
			ii[2] = Portion_dic[ii[2]]
			ii[3] = Portion_dic[ii[3]]
			ii.remove(ii[0])
			Portion_list.append(str(ii))


Compare = list(set(Complete_list+Portion_list))


try:
	assert len(Complete_dic)==len(Portion_dic)
	assert len(Complete_list)==len(Portion_list)==len(Compare)

	print '\n-----------------------------\nResult : Pass'
	print '-----------------------------\n'

except AssertionError:
	
	print 'len(Complete_dic):'
	print len(Complete_dic)
	print 'len(Portion_dic):'
	print len(Portion_dic)
	print 'len(Complete_list):'
	print len(Complete_list)
	print 'len(Portion_list):'
	print len(Portion_list)
	print 'len(Compare):'
	print len(Compare)
	print '\n-----------------------------\nResult : Fail'
	


