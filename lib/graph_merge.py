# -*- coding: utf-8 -*- 
import json,os,sys
import xml.etree.ElementTree as ET

from xml.etree.ElementTree import ElementTree
from pygraphml import Graph
from pygraphml import GraphMLParser
import GraphFun 


all_graph=[]

#creat GraphFun object
GF = GraphFun.GraphFun()

isfile = os.path.isfile(sys.argv[1])
if isfile:

	path_list = list(os.path.split(sys.argv[1]))
	all_graph=[path_list[1]]
	graph_path=path_list[0]+'/'


else:
	graph_path=sys.argv[1]+'/'

	#read graphml file
	all_file = os.listdir(graph_path)

	for i in all_file:
		if i.split(".")[-1] == 'graphml':
			all_graph.append(i)

merge_grapg = GF.multi_grapg_merge(all_graph,graph_path)

#graphml_generate
GF.graphml_generate(merge_grapg[0], merge_grapg[1], sys.argv[2]+'/merged.graphml', debug_flag=False)

