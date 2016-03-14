# -*- coding: utf-8 -*- 
import json,os,time,sys,shlex, subprocess,requests,re,thread,signal,imp
from threading import Timer
import xml.etree.ElementTree as ET
import traceback
import numpy as np

import logging
import logging.config
from subprocess import Popen, PIPE

from xml.etree.ElementTree import ElementTree


##########Set log################

logging.config.fileConfig("/usr/local/GraphwalkerRunner/logger.conf")
logger = logging.getLogger("example01")

#################################   

class GraphFun(object):

    global Interrupt_value,current_locate
    Interrupt_value=True

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

    def find_pre_replace(self,temp_list): 
    
        #find all target
             
        for i in temp_list:
            
            if type(i).__name__ == 'list':
      
                temp=self.find_pre_replace( i)
                temp_list[temp_list.index(i)]=temp
                
            else:
               
                if 'pre_' in temp_list[temp_list.index(i)]:
                    temp_list[temp_list.index(i)] = temp_list[temp_list.index(i)].strip('pre_')
        return temp_list



    def multi_grapg_merge(self, graphe_name,graph_path):

        node_count = 0
        edge_count = 0
        graph_list = []
        label_dict = {}
        all_node = []
        all_edge = []
        node_list_final = []
        edge_list_final = []
        
        #read all graph
        for graph_item in graphe_name:
            match_dict = {}

            #read graph 
            graph = self.read_graphml(graph_path,graph_item)

            #取得所有節點id
            for node_id in graph[0]:
                
                #add replace dict
                match_dict[node_id[0]] = 'n'+str(node_count)

                #替換節點名稱 

                graph[0] = self.find_Next_Floor(node_id[0], 'pre_n'+str(node_count), graph[0])
         
                #疊加節點id序號
                node_count+=1
                
            #取得所有邊id
            for edge_id in graph[1]:
            
                #替換邊名稱 
                graph[1] = self.find_Next_Floor(edge_id[0], '"e'+str(edge_count), graph[1])
               
                #替換節點id序號
                if match_dict.has_key(edge_id[2]):

                    graph[1] = self.find_Next_Floor(edge_id[2], 'pre_'+str(match_dict[edge_id[2]]), graph[1])

                if match_dict.has_key(edge_id[3]):
    
                    graph[1] = self.find_Next_Floor(edge_id[3], 'pre_'+str(match_dict[edge_id[3]]), graph[1])

                #疊加邊id序號
                edge_count+=1
            
            graph_list.append(graph)


        #結合所有的節點和邊
        
        for graph_item in graph_list:
            all_node+=graph_item[0]
            all_edge+=graph_item[1]
        graph_all=[all_node,all_edge]
        

        #replace 'pre' node name
        graph_all = self.find_pre_replace(graph_all)

        #replace id
        for graph_item in graph_all:
              
            for item in graph_item: 
                
                if  label_dict.has_key(item[1]) and label_dict[item[1]] !=  item[0]:
                    graph_all = self.find_Next_Floor(item[0], label_dict[item[1]], graph_all)
                else:

                    label_dict[item[1]] = item[0]
                

        #del duplicate node
        for node_item in graph_all[0]:

            if node_item not in node_list_final:
                node_list_final.append(node_item)

        #del duplicate edge
        for edge_item in graph_all[1]:

            if edge_item not in edge_list_final:
                edge_list_final.append(edge_item)

        graph_all[0] = node_list_final
        graph_all[1] = edge_list_final

        return graph_all

    def Count_Walked(self, stop_condition="random(edge_coverage(100))"):
        Walked_list = []

        #path_result = os.popen("java -jar /usr/local/GraphwalkerRunne/lib/graphwalker-cli-SNAPSHOT.jar offline --json -m /usr/local/GraphwalkerRunner/lib/merged_mark.graphml \""+stop_condition+"\"").read()
        try:

            p = Popen(['java','-jar','/usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar','offline','--json','-m','/usr/local/GraphwalkerRunner/lib/merged_mark.graphml','"'+stop_condition+'"'],stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
            output, error = p.communicate()

            if p.returncode == 0:
                ok=True if output else False        
            else:
                ok=False

            assert ok==True,error

        except Exception as e:

            logger.error(str(e))

        return output



    def kill_Process(self,grep_name='graphwalker-cli-SNAPSHOT.jar'):

        #kill process---------------- 
        # result = os.popen("ps -ef |grep 'graphwalker-cli-SNAPSHOT.jar' | awk '{print $2,$8}'").read()
        result = os.popen("ps -ef |grep '"+grep_name+"' | awk '{print $2,$8}'").read()

        for i in result.split('\n'):
            if 'java' in i:
                print 'kill pid : '+i.split(' ')[0]
                os.popen("kill -9 "+i.split(' ')[0])
            elif 'python' in i:
                print 'kill pid : '+i.split(' ')[0]
                os.popen("kill -9 "+i.split(' ')[0])
            elif 'Graphwalker_Runner' in i:
                print 'kill pid : '+i.split(' ')[0]
                os.popen("kill -9 "+i.split(' ')[0])

        

    def Run_Websocket(self,stop_condition='random(edge_coverage(100))'):

        #Run websocket----------------
        print 'Run websocket...'
        pid = os.popen('java -jar /usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar online --json --service RESTFUL -m /usr/local/GraphwalkerRunner/lib/merged_mark.graphml \"'+stop_condition+'\" &')

        time.sleep(5)

    def Add_BLOCKED(self,graph_path, path,Fail_Fun):

        graph = self.read_graphml(graph_path,path)
        for graph_item in graph:
            for item in graph_item:
                if Fail_Fun in item[1]:
                    error_v = item[1].split('\n')
                    if 'BLOCKED' not in error_v:
                        error_v.append('BLOCKED')
                        join_str = '\n'.join(error_v)
                        item[1]=join_str

        return graph

    def Stop_Condition(self,c_locate,timeout=300):
        step_count_list=[]

        for i in range(10):
            result = self.timeout('Count_Walked',c_locate,timeout)
            if result:
                step = result.count('CurrentElementName')
                step_count_list.append(int(step))
                if i==0:
                    print 'The '+str(i+1)+'st times step:'+str(step)
                elif i==1:
                    print 'The '+str(i+1)+'nd times step:'+str(step)
                elif i==2:
                    print 'The '+str(i+1)+'rd times step:'+str(step)
                else:
                    print 'The '+str(i+1)+'th times step:'+str(step)
            else:
                break

        assert step_count_list,'Stop_Condition all timeout'

        Average = np.mean(step_count_list)
        Std = np.std(step_count_list)
        Max = max(step_count_list)
        Min = min(step_count_list)
        Stop = Max + Min * 2
        print 'Step List:'+str(step_count_list)+'\nMax:'+str(Max)+'\nMin:'+str(Min)+'\nStop Condition:'+str(Stop)


        return Max,Min,Stop

    def Screenshot(self, display_num, step):

        print 'Save Screenshot...'

        if not os.path.exists(c_locate+'/Screenshot'):
            os.popen('mkdir '+c_locate+'/Screenshot') 

        os.popen('import -display :'+str(display_num)+' -window root '+c_locate+'/Screenshot/'+step+'.png') 


    def BLOCKED_Exception_Action(self, Error_Type, e, BLOCKED, Max, Min,step, NoneError ,Test_result):

        print '\nStep('+Error_Type+') occured error:\n'+str(e)+'\n'

        #self.Screenshot(0,step)

        #add new key
        if not BLOCKED.has_key(Error_Type):
            BLOCKED[Error_Type]=[]

        BLOCKED[Error_Type].append(str(step))

        Stop = Max + Min * 2

        NoneError = not NoneError

        Test_result['Fail_Fun'] = str(step)

        return BLOCKED, Stop, NoneError, Test_result

    def Fun_Exception_Action(self, e, Max, Min, step, NoneError,Test_result,step_list,error_list,current_locate,argv_4):

        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        time.sleep(0.5)
        error_msg = '\nAction error on '+str(step)+'\nError content:'+str(sys.exc_info())+'\nError line:'+str(line)+'\nError Func:'+str(func)+'\nError text:'+str(text)+'\n'
        print error_msg
        
        #self.Screenshot(0,step)

        Stop = Max + Min * 2
        NoneError = not NoneError
        Test_result['Fail_Fun'] = str(step)
        Test_result['Error_Message'] = error_msg

        #append error path
        step_str = '->'.join(step_list)
        Test_result['step'] = step_str
        error_list.append(Test_result)

        #Saving Logcat info
        if argv_4:
            result_log = self.save_log(current_locate)
            if result_log:
                Test_result['Android_Log'] = result_log

        return Stop,NoneError,Test_result,error_list

    def Connection_Aborted(self,e,stop_condition='random(edge_coverage(100))'):

        print 'Connection aborted....'

        command_line = "java -jar /usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar online --json --service RESTFUL -m /usr/local/GraphwalkerRunner/lib/merged_mark.graphml \""+stop_condition+"\""

        args = shlex.split(command_line)

        sp = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        out, err = sp.communicate()

        if err:
            error = err.split('\n')[-3].split(': \'')
            root_cause = error[0]
            step = error[-1][:-1]

            return root_cause,step

    def interrupt(self):
        
        thread.interrupt_main()
        

    def timeout(self,fun_name,c_locate,timeout=300):

        global current_locate
        current_locate = c_locate

        try:
            t = Timer(int(timeout), self.interrupt)
            t.start()
            result = eval( 'self.'+fun_name + "()" )
            t.cancel()
            return result

        except KeyboardInterrupt as e:
            logger.error(str('[Timeout] :')+str(fun_name))
            print 'KeyboardInterrupt'
            print '\n-------------------------\nPlease click enter to end...\n-------------------------\n'
            self.kill_Process('Runner.py')
            self.kill_Process('')

    def save_log(self,current_locate,serial=''):


        try:
            logger.info('Log Saving...')
            timestamp = time.strftime("%Y%m%d%H%M%S")

            # local_path = os.getcwd() + '/log/' + timestamp
            local_path = current_locate + '/log/' + timestamp

            os.popen('mkdir -p ' + local_path)


            if serial != '':

                serial = '-s ' + serial

            logcat_file = local_path + '/logcat_' + timestamp + '.log'

            os.popen('adb ' + serial + ' shell logcat -v time -d > ' + logcat_file)   

            logcat_file = local_path + '/dmesg_' + timestamp + '.log'
            os.popen('adb ' + serial + ' shell dmesg > ' + logcat_file)

            logcat_file = local_path + '/bugreport_' + timestamp + '.log'
            os.popen('adb ' + serial + ' bugreport > ' + logcat_file)

            os.popen('adb ' + serial + ' shell logcat -c')           

            #check crash log
            retval = os.popen("cat " + logcat_file + " | grep 'beginning\ of\ crash' | wc -l").read().strip()
            if retval != '0':
                return "[CRASH]" + timestamp
            else:
                return "[MINOR]" + timestamp

            logger.info('Log Saved')

        except Exception as e:

            logger.error(str    )

            return False

    def screen_shot(self,argv,sys_argv,command,step_count,step):

      

        if argv == 'mobile':
            os.system("adb shell screencap -p /sdcard/screen.png")
            os.system("adb pull /sdcard/screen.png "+sys_argv+'/Screenshot/'+command+'/screen-'+step_count+'-'+step+'.png > /dev/null 2>&1 ')
            os.system("adb shell rm /sdcard/screen.png")
            # os.system("adb shell screencap -p | sed 's/\r$//' > "+sys_argv+'/Screenshot/'+command+'/screen-'+step_count+'-'+step+'.png')
            
        elif argv == 'pc':
            os.system('import -display :0 -window root '+sys_argv+'/Screenshot/'+command+'/screen-'+step_count+'-'+step+'.png')
            
    


    def CheckGraphicalIntegrity(self):

        global current_locate
        # read file & get fun name & write to file
        try:
            func_list = []
            count=0
            w_file = open(current_locate+'/script_test.py', 'w')
            with open(current_locate+'/script.py', 'r') as file:
             
                for line in file:
                    if re.match('^#',line):
                        continue
                    elif 'def ' in line:
                        func_list.append(line[4:-5])
                        w_file.write(line)
                        w_file.write('\n')
                        w_file.write('  return "'+str(line[4:-5])+'"')
                        w_file.write('\n')
            w_file.close()
       
            fun_list_len = len(func_list)

            #Checking Graphical Integrity
            # print 'Checking...'
            

            # import script_test as RunFun
            RunFun = imp.load_source('script_test', current_locate+'/script_test.py')

            self.kill_Process() 
           
            # logger.info(str('Checking Graphical Integrity by offline'))
            # p = Popen(['java','-jar','/usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar','offline','--json','-m',current_locate+'/merged.graphml','"random(edge_coverage(100))"'],stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
            # output, error = p.communicate()

            # if p.returncode == 0:
            #     ok=True if output else False        
            # else:
            #     ok=False

            # assert ok==True,error
            # logger.info(str('successful'))

            logger.info(str('Run Websocket...'))

            

            command = 'sudo fuser 8887/tcp > port_used_list.txt'

            os.popen(command)
            time.sleep(1)
            port_list=[]

            port = open('port_used_list.txt','r')
            for line in port.readlines():
                port_list.append(line.strip())
                logger.error('port is used. id:'+str(line.strip()))

            assert port_list==[],'port is used.'
            os.popen('rm port_used_list.txt')
            os.popen('java -jar /usr/local/GraphwalkerRunner/lib/graphwalker-cli-SNAPSHOT.jar online --json --service RESTFUL -m '+current_locate+'/merged.graphml \"random(edge_coverage(100))\" &')
            time.sleep(5)

            logger.info(str('Checking every point by online'))
            gw_url = 'http://localhost:8887/graphwalker'

            while requests.get(gw_url+'/hasNext').json()['HasNext'] == 'true' :
        
                step = requests.get(gw_url+'/getNext').json()['CurrentElementName']

                if step != '' :

                    result = eval( "RunFun."+ step + "()" )
                    
                    len_before = len(func_list)

                    if result in func_list:
                    
                        func_list.remove(result)
                        
                    error_file = open(current_locate+'/Not_visited_points.txt', 'w')
                    error_file.write(str(func_list))
                    error_file.close()

                    len_after = len(func_list)

                    if len_before == len_after:
                        count+=1
                    else:
                        count=0
                    if count == fun_list_len * fun_list_len:
                        logger.info(str('===============Result==================='))
                        logger.info(str('Visited incomplete graphics'))
                        logger.info(str('Stop Condition is (length * length) Step'))
                        logger.info(str('========================================'))
                        break
            
            if count < fun_list_len * fun_list_len:

                logger.info(str('===========Result============='))
                logger.info(str('Visited complete graphics'))
                logger.info(str('=============================='))

                        
            if func_list:
                logger.info(str('Not visited points : '))
                logger.info(func_list)
                logger.info(str('Output log file : Not_visited_points.txt'))
                logger.info('log file path : '+current_locate+'/Not_visited_points.txt')

                error_file = open(current_locate+'/Not_visited_points.txt', 'w')
                error_file.write(str(func_list))
                error_file.close()
            else:
        
                p = Popen(['rm',current_locate+'/Not_visited_points.txt'], stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
                output, error = p.communicate()
                if p.returncode == 0:
                    if output:
                        if output_file:
                            with open(output_file, 'w') as outfile:
                                outfile.write(str(output))
                        else:
                            logger.info(output)
                else:
                    logger.error(str(error))          

            # os.popen('rm /usr/local/GraphwalkerRunner/lib/script_test.py /usr/local/GraphwalkerRunner/lib/script_test.pyc')
            
            return func_list if func_list else True

        except Exception as e:
            logger.error(str(e))

            # print '\n-------------------------\nException\n-------------------------\n'
            self.kill_Process()
            return e 
    
    def Test_Report(self, complete_value, error_list, pass_dic, BLOCKED):
        logger.info(str('Generate Test Report'))

        try:

            #All Pass
            if pass_dic['Completion_type'] == 'Pass':

                with open('test_report.txt', 'w') as report_file:

                    report_file.write('[PASS]\n\tSTEP : ')

                    ste_list = ' -> '.join(pass_dic['ste_list'])
                    report_file.write(str(ste_list))

            #Conditional Pass
            elif pass_dic['Completion_type'] == 'Fail':

                with open('test_report.txt', 'w') as report_file:

                    report_file.write('[Fail Record]\n\n')

                    #create fail testcase
                    report_file.write('\t[Error]\n\n')
                    for i in error_list:

                        report_file.write('\t\tFail_Fun : '+str(i['Fail_Fun'])+'\n')
                        if i.has_key('Android_Log'):
                            report_file.write('\t\tAndroid_Log : '+str(i['Android_Log'])+'\n')
                        report_file.write('\t\tstep : '+str(i['step'])+'\n')
                        report_file.write('\t\tError_Message : '+str(i['Error_Message'])+'\n\n')
                        

                    #create pass testcase
                    report_file.write('\t[Conditional Pass]\n')
        
                    report_file.write('\n\t\tstep : '+pass_dic['step_str']+'\n\n')

                    #create ignore testcase

                    if BLOCKED.has_key('getNext'):

                        report_file.write('\t[Ignore]\n')

                        report_file.write('\n\t\tpoint : '+str(BLOCKED['getNext'])+'\n\n')                    


        except Exception as e:

            logger.error(str(e))

    def Generate_XML(self, complete_value, error_list, pass_dic, BLOCKED):

        logger.info(str('Generate XML'))
        
        try:

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

                    testcase = ET.SubElement(testsuite,"testcase" ,message='complete Condition:'+str(complete_value),classname='Fail',name=str(i['Fail_Fun']))

                    img = 'http://192.168.20.140:8080/jenkins/job/MBT_Project/job/JUSTUP/ws/Graphwalker/Run_GraphWalker/Screenshot/'+str(i['Fail_Fun'])+'.png'
                    if i.has_key('Android_Log'):
                        message_str='step : '+str(i['step'])+'\n\nError_Message : '+str(i['Error_Message'])+'\n\nFail_Fun : '+str(i['Fail_Fun'])+'\n\nAndroid_Log : '+str(i['Android_Log'])
                    else:
                        message_str='step : '+str(i['step'])+'\n\nError_Message : '+str(i['Error_Message'])+'\n\nFail_Fun : '+str(i['Fail_Fun'])
                    ET.SubElement(testcase,"error" ,message=str(message_str)+' \n\nScreenshot : '+str(img))
                    
                

                #create pass testcase
                for i in pass_dic['ste_list']:

                    testcase = ET.SubElement(testsuite,"testcase" ,classname='pass',name=str(i))

                    ET.SubElement(testcase,"pass")

                #create ignore testcase

                for item in BLOCKED:

                    for i in BLOCKED[item]:

                        testcase = ET.SubElement(testsuite,"testcase" ,classname='ignore',name=str(i))

                        ET.SubElement(testcase,"skipped",message='Ignore HasNext Messages : ' + str(i),name=str(item) )

               
        

            tree = ET.ElementTree(testsuite)


            tree.write("Result.xml", 'UTF-8', 'True')
            

        except Exception as e:
            logger.error(str(e))