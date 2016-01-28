# -*- coding: utf-8 -*- 
import json,os,sys
import xml.etree.ElementTree as ET

from xml.etree.ElementTree import ElementTree
from pygraphml import Graph
from pygraphml import GraphMLParser
import GraphFun 

#graph_path='./Justup_2/'
graph_path=sys.argv[1]+'/'

#creat GraphFun object
GF = GraphFun.GraphFun()


#read graphml file

all_graph = os.listdir(graph_path)

merge_grapg = GF.multi_grapg_merge(all_graph,graph_path)

#graphml_generate
GF.graphml_generate(merge_grapg[0], merge_grapg[1], sys.argv[2]+'/merged.graphml', debug_flag=False)

