# -*- coding: utf-8 -*- 
import json,os,time,sys
import xml.etree.ElementTree as ET
import numpy as np

from xml.etree.ElementTree import ElementTree



class GraphFun(object):

    def make_fun(self,merge_grapg):

        all_fun=[]

     
        for graph_item in merge_grapg:
            for item in graph_item:
                all_fun.append(item[1].split('\n'))
       
        fun_str='#!/usr/bin/env python \n# -*- coding: utf-8 -*-\n\nfrom selenium import webdriver\nimport time\nfrom selenium.webdriver.common.by import By\n\nglobal driver\n\n\n'

        write_path = open('fun/merge_fun.py', "w")
        
        for fun_item in all_fun:

            fun_str += 'def '+str(fun_item[0])+'():\n    global driver\n'
            for parameter in fun_item[1:]:
        
                fun_str += '    '+parameter+'\n'
                

            fun_str+='\n\n'

        write_path.write(fun_str)

        write_path.close()

    def read_graphml(self,graph_path, path):

        graphml_1 = open(graph_path+path,'r')
        graphml_1_all_text = graphml_1.read()
        graphml_1_all_data = self.deserialize(graphml_1_all_text)

        return graphml_1_all_data
  
    def deserialize(self, d):
    
        y = '{http://www.yworks.com/xml/graphml}'
        ns = '{http://graphml.graphdrawing.org/xmlns}'
        nodestr = './/' + ns + 'node'
        edgestr = './/' + ns + 'edge'

        doc = ET.fromstring(d)
        verts, edges = [], []

        for n in doc.findall('.//' + ns + 'node'):
            l = n.find('.//' + y + 'NodeLabel')
            if l is None:
                continue

            verts.append([n.attrib['id'], l.text.strip()])

        for n in doc.findall('.//' + ns + 'edge'):
            l = n.find('.//' + y + 'EdgeLabel')
            e_id = n.attrib['id']
            e_name = l.text.strip() if l is not None else None
            e_src = n.attrib['source']
            e_tgt = n.attrib['target']
            edges.append([e_id, e_name, e_src, e_tgt])

        return [verts, edges]

    def graphml_generate(self, node_list, edge_list, out_name, debug_flag=False):
        # node & edge tuple list sample
        #[('n1', 'v_node_a'), ('n2', 'v_node_b')]
        #[('e0', 'NONE', 'n0', 'n1'), ('e1', 'e_home', 'n2', 'n1')]

        ns_list = {'gns': '{http://graphml.graphdrawing.org/xmlns}',
                  'yns': '{http://www.yworks.com/xml/graphml}'}

        elm_root = ET.Element('graphml', xmlns=ns_list['gns'].strip('{}'))
        elm_root.set('xmlns:y', ns_list['yns'].strip('{}'))
        elm_share_key = ET.SubElement(elm_root, 'key', id="d6")
        elm_share_key.set('yfiles.type', "nodegraphics")
        elm_share_key = ET.SubElement(elm_root, 'key', id="d10")    
        elm_share_key.set('for', "edge")
        elm_share_key.set('yfiles.type', "edgegraphics")    

        elm_graph = ET.SubElement(elm_root, 'graph', edgedefault="directed", id="G")

        for n in node_list:
            elm_node_tmp = ET.SubElement(elm_graph, 'node', id=n[0])
            elm_node_data = ET.SubElement(elm_node_tmp, 'data', key="d6")
            elm_node_data_SN = ET.SubElement(elm_node_data, 'y:ShapeNode')
            elm_node_data_NL = ET.SubElement(elm_node_data_SN, 'y:NodeLabel')
            elm_node_data_NL.text = n[1]

        for n in edge_list:
            elm_edge_tmp = ET.SubElement(elm_graph, 'edge', id=n[0], source=n[2], target=n[3])
            elm_edge_data = ET.SubElement(elm_edge_tmp, 'data', key="d10")
            elm_edge_data_PLE = ET.SubElement(elm_edge_data, 'y:PolyLineEdge')
            if n[1] is not "NONE":
                elm_edge_data_PLE_EL = ET.SubElement(elm_edge_data_PLE, 'y:EdgeLabel') 
                elm_edge_data_PLE_EL.text = n[1]

        tree_root = ElementTree()
        tree_root._setroot(elm_root)
        tree_root.write(out_name, 'UTF-8', 'True')

        if debug_flag is True:
            print 'Node_List:'
            for n in node_list:
                print n
            print '\nEdge_List:' 
            for n in edge_list:
                print n
            print '\nElementTree Dump:'
            ET.dump(elm_root)
            print '\nTree Dump:'
            for child in tree_root.iter():
                print child.tag, child.attrib

    def combine(self,graphml_1,graphml_2):


        repace_list = {}
        del_list=[]
        match_count = 0

        #read txt & replace value
        G1_txt = json.dumps(graphml_1)
        G2_txt = json.dumps(graphml_2)

        G1 = json.loads(G1_txt)
        G2 = json.loads(G2_txt) 

        
        G1_node_len = len(graphml_1[0])
        G1_dege_len = len(graphml_1[1])

        # reset node number & replace duplicate node id
        for G2_node in G2[0]:

            T=True

            for G1_node in G1[0]:

                if G1_node[1] == G2_node[1]:

                    match_count+=1
                    re_str = '<re_duplicate>' + str(match_count)

                    G2_txt = G2_txt.replace(G2_node[0],re_str)
                    del_list.append(G1_node)
                    repace_list[re_str]=G1_node[0]

                    T=False
                
            if T:


                re_str = '<re_node>' +str(G1_node_len)

                G2_txt = G2_txt.replace(G2_node[0],re_str)

                repace_list[re_str]='n'+str(G1_node_len)
                G1_node_len += 1

        #reset edge number
        for G2_egde in G2[1]:
           
            
            re_str = '<re_edge>' +str(G1_dege_len)

            G2_txt = G2_txt.replace(G2_egde[0], re_str)
        
            repace_list[re_str]='e' +str(G1_dege_len)
            G1_dege_len += 1

        #replace repace_list all element
        for repace_item in repace_list:
         
            G2_txt = G2_txt.replace(repace_item,repace_list[repace_item])

        #str to list
        G1 = json.loads(G1_txt)
        G2 = json.loads(G2_txt) 


        for del_item in del_list:
            G2[0].remove(del_item)

        #combine node...
        combine_node = G1[0]+G2[0]

        #combine edge...

        combine_edge = G1[1]+G2[1]
     

        return (combine_node,combine_edge)

   

    def find_Next_Floor(self, key_word, replace_word, temp_list): 
    
        #find all target
             
        for i in temp_list:
            
            if type(i).__name__ == 'list':
      
                temp=self.find_Next_Floor(key_word, replace_word, i)
                temp_list[temp_list.index(i)]=temp
                
            else:
               
                if temp_list[temp_list.index(i)] == key_word:
                    temp_list[temp_list.index(i)]=replace_word
        return temp_list



    def multi_grapg_merge(self, graphe_name,graph_path):

        node_count = 0
        edge_count = 0
        graph_list = []
        match_dict = {}
        label_dict = {}
        all_node = []
        all_edge = []
        node_list_final = []
        edge_list_final = []
   
        #read all graph
        for graph_item in graphe_name:

            #read graph 
            graph = self.read_graphml(graph_path,graph_item)

            #取得所有節點id
            for node_id in graph[0]:

                #add replace dict
                match_dict[node_id[0]] = 'n'+str(node_count)
                    
                #替換節點名稱 
                graph[0] = self.find_Next_Floor(node_id[0], 'n'+str(node_count), graph[0])

                #疊加節點id序號
                node_count+=1
           
            #取得所有邊id
            for edge_id in graph[1]:
                
                #替換邊名稱 
                graph[1] = self.find_Next_Floor(edge_id[0], '"e'+str(edge_count), graph[1])
                
                #替換節點id序號
                if match_dict.has_key(edge_id[2]):
                    graph[1] = self.find_Next_Floor(edge_id[2], match_dict[edge_id[2]], graph[1])
                if match_dict.has_key(edge_id[3]):
                    graph[1] = self.find_Next_Floor(edge_id[3], match_dict[edge_id[3]], graph[1])

                #疊加邊id序號
                edge_count+=1
   
            graph_list.append(graph)
            
        #結合所有的節點和邊
        
        for graph in graph_list:
            all_node+=graph[0]
            all_edge+=graph[1]
        graph=[all_node,all_edge]
       
        #replace id
        for graph_item in graph:
              
            for item in graph_item: 
                
                if  label_dict.has_key(item[1]) and label_dict[item[1]] !=  item[0]:

                    graph = self.find_Next_Floor(item[0], label_dict[item[1]], graph)
                else:

                    label_dict[item[1]] = item[0]
            print '\n'

        #del duplicate node
        for node_item in graph[0]:

            if node_item not in node_list_final:
                node_list_final.append(node_item)

        #del duplicate edge
        for edge_item in graph[1]:

            if edge_item not in edge_list_final:
                edge_list_final.append(edge_item)

        graph[0] = node_list_final
        graph[1] = edge_list_final

        return graph

    def Count_Walked(self, stop_condition):
        if stop_condition == '':

            stop_condition="random(edge_coverage(100))"

        Walked_list = []
        path_result = os.popen("java -jar graphwalker-cli-3.4.0-SNAPSHOT.jar offline --json -m merger.graphml \""+stop_condition+"\"").read()
        
        return path_result



    def kill_Process(self):

        #kill process---------------- 
        result = os.popen("ps -ef |grep 'graphwalker-cli-3.4.0-SNAPSHOT.jar' | awk '{print $2,$8}'").read()
        
        for i in result.split('\n'):
            if 'java' in i:
                print 'kill pid : '+i.split(' ')[0]
                os.popen("kill -9 "+i.split(' ')[0])
        
        time.sleep(1)

    def Run_Websocket(self,blocked_exist):

        #Run websocket----------------
        print 'Run websocket...'
        
        if blocked_exist:
            
            pid = os.popen('java -jar graphwalker-cli-3.4.0-SNAPSHOT.jar online --json --service RESTFUL -m merger.graphml \"random(edge_coverage(100))\" &')

        else:
            pid = os.popen('java -jar graphwalker-cli-3.4.0-SNAPSHOT.jar online --json --service RESTFUL -m merger.graphml \"random(edge_coverage(100))\" &')

        time.sleep(5)

    def Add_BLOCKED(self,graph_path, path,Fail_Fun):
        graph = self.read_graphml(graph_path,path)
        for graph_item in graph:
            for item in graph_item:
                if Fail_Fun in item[1]:
                    error_v = item[1].split('\n')
                    error_v.append('BLOCKED')
                    join_str = '\n'.join(error_v)
                    item[1]=join_str

        return graph

    def Stop_Condition(self):
        step_count_list=[]

        for i in range(10):
            
            step = self.Count_Walked('random(edge_coverage(100))').count('CurrentElementName')
            step_count_list.append(int(step))
            print 'The '+str(i+1)+' times step:'+str(step)

        Average = np.mean(step_count_list)
        Std = np.std(step_count_list)
        Max = max(step_count_list)
        Min = min(step_count_list)
        Stop = Max + Min * 2
        print 'Step List:'+str(step_count_list)+'\nMax:'+str(Max)+'\nMin:'+str(Min)+'\nStop Condition:'+str(Stop)


        return Max,Min,Stop

    def BLOCKED_Exception_Action(self, Error_Type, e, BLOCKED, Max, Min,step, NoneError ,Test_result):

        print '\nStep('+Error_Type+') occured error:\n'+str(e)+'\n'
        BLOCKED['getNext'].append(str(step))
        Stop=Max+Min*2
        NoneError = not NoneError
        Test_result['Fail_Fun'] = str(step)

        return BLOCKED, Stop, NoneError, Test_result

    def Fun_Exception_Action(self, e, Max, Min, step, NoneError,Test_result,step_list,error_list):

        print '\nAction error on '+str(step)+'\nError message:\n'+str(e)+'\n'
        Stop = Max + Min * 2
        NoneError = not NoneError
        Test_result['Fail_Fun'] = str(step)
        Test_result['Error_Message'] = sys.exc_info()

        #append error path
        step_str = '->'.join(step_list)
        Test_result['step'] = step_str
        error_list.append(Test_result)

        return Stop,NoneError,Test_result,error_list

    def Generate_XML(self, complete_value, error_list, pass_dic, BLOCKED):

        print 'Generate_XML'

        testsuite = ET.Element("testsuite", Tests=str(len(error_list)))

        properties = ET.SubElement(testsuite,"properties")

        
        index = 0

        #All Pass
        if pass_dic['Completion_type'] == 'Pass':

            testcase = ET.SubElement(testsuite,"testcase" ,classname='All',name='Pass')

            ET.SubElement(testcase,"Pass" ,message='The Step :\n '+str(pass_dic['step_str']))

            #create pass testcase
            for i in pass_dic['ste_list']:

                testcase = ET.SubElement(testsuite,"testcase" ,classname='pass',name=str(i))

                ET.SubElement(testcase,"pass")

        #Conditional Pass
        elif pass_dic['Completion_type'] == 'Fail':

            #create fail testcase
            for i in error_list:

                index+=1
                index_str = str(index)
                zfill = index_str.zfill(4)

                testcase = ET.SubElement(testsuite,"testcase" ,message='complete Condition:'+str(complete_value),classname='Fail',name=zfill)

                message_str='step : '+str(i['step'])+'\n\nError_Message : '+str(i['Error_Message'])+'\n\nFail_Fun : '+str(i['Fail_Fun'])
                ET.SubElement(testcase,"error" ,message=str(message_str))

            #create pass testcase
            for i in pass_dic['ste_list']:

                testcase = ET.SubElement(testsuite,"testcase" ,classname='pass',name=str(i))

                ET.SubElement(testcase,"pass")

            #create ignore testcase


            if BLOCKED.has_key('HasNext'):

                for i in BLOCKED['HasNext']:

                    testcase = ET.SubElement(testsuite,"testcase" ,classname='ignore',name=str(i))

                    ET.SubElement(testcase,"skipped",message='Ignore HasNext Messages : ' + str(i),name='HasNext' )

            if BLOCKED.has_key('getNext'):

                for i in BLOCKED['getNext']:

                    testcase = ET.SubElement(testsuite,"testcase" ,classname='ignore',name=str(i))

                    ET.SubElement(testcase,"skipped",message='Ignore getNext Messages : ' + str(i),name='getNext' )

    

        tree = ET.ElementTree(testsuite)


        tree.write("Result.xml", 'UTF-8', 'True')
       

