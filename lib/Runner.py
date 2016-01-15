
# -*- coding: utf-8 -*-
import requests,json,traceback,time,sys,os
import GraphFun as GraphFun
import script as RunFun

global temp
temp={}









#init parameter
NoneError = True
Pid_exist = True
blocked_exist = True
error_list = []
pass_dic = {}
BLOCKED = {}

#creat GraphFun object----------------
GF = GraphFun.GraphFun()

#rename graphml (merged.graphml -> merged_mark.graphml)
#print 'rename graphml... (merged.graphml -> merged_mark.graphml)'
os.popen('cp merged.graphml /usr/local/GraphwalkerRunner/lib/merged_mark.graphml')

print 'Get average count...'
Max,Min,Stop = GF.Stop_Condition(sys.argv[1])

test_count=0


if not os.path.exists(sys.argv[1]+'/Screenshot'):
    os.popen('mkdir '+sys.argv[1]+'/Screenshot')
else:
    os.popen("rm -rf "+sys.argv[1]+"/Screenshot")
    os.popen('mkdir '+sys.argv[1]+'/Screenshot')


while(NoneError):
    step_count=0

    if test_count==0:
        command =  'The\ '+str(test_count+1)+'st\ times\ testing'
    elif test_count==1:
        command =  'The\ '+str(test_count+1)+'nd\ times\ testing'
    elif test_count==2:
        command =  'The\ '+str(test_count+1)+'rd\ times\ testing'
    else:
        command =  'The\ '+str(test_count+1)+'th\ times\ testing'

    os.popen('mkdir '+sys.argv[1]+'/Screenshot/'+str(command))
    
    test_count+=1

    print '\nRun Testing...\n'
    GF.kill_Process() 

    GF.Run_Websocket(blocked_exist)  

    gw_url = 'http://localhost:8887/graphwalker'

    step_list=[]
    Test_result = {}

    #Run Graphwalker----------------
    try:
        while requests.get(gw_url+'/hasNext').json()['HasNext'] == 'true' and Stop > 0 :

            # Get next step from GraphWalker
            try:

                step = requests.get(gw_url+'/getNext').json()['CurrentElementName']

            # Step(CurrentElementName) occured error
            except Exception as e:
                print e
                # BLOCKED Error Handling 
                BLOCKED,Stop,NoneError,Test_result = GF.BLOCKED_Exception_Action('getNext', e, BLOCKED, Max, Min, step, NoneError,Test_result)
                break

            step_list.append(str(step))

            #Run Function
            if step != '' :
                try:
                    eval( "RunFun."+step + "()" )
                    Stop-=1

                    if sys.argv[2] == 'mobile':
                        os.system("adb shell screencap -p | sed 's/\r$//' > "+sys.argv[1]+"/Screenshot/"+command+"/screen-" + str(step_count) + "-" + step + ".png")
                    else:
                        os.popen('import -display :0 -window root '+sys.argv[1]+'/Screenshot/'+command+'/screen-' + str(step_count) + '-' + step + '.png') 
                    
                    step_count+=1

                #Fun error
                except Exception as e:
                    print e
                    #Fun error Handling
                    Stop,NoneError,Test_result,error_list = GF.Fun_Exception_Action(e, Max, Min, step, NoneError,Test_result,step_list,error_list)
                    break

        # integrate screen capture code to templete
        if sys.argv[2] == 'mobile':
            os.system("adb shell screencap -p | sed 's/\r$//' > "+sys.argv[1]+"/Screenshot/"+command+"/screen_final.png")
        else:
            os.popen('import -display :0 -window root '+sys.argv[1]+'/Screenshot/'+command+'/screen_final.png') 
        # integrate cleanup code to templete
        #RunFun.temp['driver'].quit()

    # Step(HasNext) occured error
    except Exception as e:
        print e
        #occured Connection aborted error
        if  'Connection refused' in str(e):
            print 'Connection refused'
            root_cause,step = GF.Connection_Aborted(e)
            print root_cause,step

        else:
            root_cause = 'HasNext'

        print '----------'
        # BLOCKED Error Handling
        BLOCKED,Stop,NoneError,Test_result = GF.BLOCKED_Exception_Action(root_cause, e, BLOCKED, Max, Min, step, NoneError,Test_result)


    if(not NoneError):
        #Add BLOCKED----------------
        graph = GF.Add_BLOCKED('/usr/local/GraphwalkerRunner/lib/', 'merged_mark.graphml',Test_result['Fail_Fun']) 

        #graphml_generate----------------
        GF.graphml_generate(graph[0], graph[1], '/usr/local/GraphwalkerRunner/lib/merged_mark.graphml', debug_flag=False)

    NoneError = not NoneError
       


#complete Condition
complete_value = 'Condition Completion' if Stop == 0 else 'Full Completion'

step_str = ' -> '.join(step_list)
pass_dic['step_str'] = step_str
pass_dic['ste_list'] = list(set(step_list))
pass_dic['Completion_type']='Fail' if len(error_list) > 0 else 'Pass'


   

print '\n\n*********************\n'+str(complete_value)+'\n*********************'

print '\n\n*********************\n'+str(BLOCKED)+'\n*********************'

#Generate XML
GF.Generate_XML(complete_value, error_list,pass_dic,BLOCKED)

