
# -*- coding: utf-8 -*-
import requests,json,traceback,time,sys,os
import lib.GraphFun as GraphFun
import script as RunFun

global temp
temp={}



VaildGraph = False





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
print 'rename graphml... (merged.graphml -> merged_mark.graphml)'
os.popen('cp merged.graphml merged_mark.graphml')

#Check graphical integrity
print 'Check graphical integrity'
result = GF.CheckGraphicalIntegrity()
print result

# assert result==True,'Graphics incomplete'

#Get average count
print 'Get average count...'
Max,Min,Stop = GF.Stop_Condition()

step_count = 0
os.system("rm Screenshot/*.png")

while(NoneError):

    
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

                    # TODO: integrate screen capture code to templete
                    os.system("adb shell screencap -p | sed 's/\r$//' > Screenshot/screen-" + str(step_count) + "-" + step + ".png")

                    step_count+=1
            
                #Fun error
                except Exception as e:
                    print e
                    #Fun error Handling
                    Stop,NoneError,Test_result,error_list = GF.Fun_Exception_Action(e, Max, Min, step, NoneError,Test_result,step_list,error_list)
                    break
        # TODO: integrate screen capture code to templete
        os.system("adb shell screencap -p | sed 's/\r$//' > Screenshot/screen_final.png")
        # TODO: integrate cleanup code to templete
        RunFun.temp['driver'].quit()


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
        graph = GF.Add_BLOCKED('./', 'merged_mark.graphml',Test_result['Fail_Fun']) 

        #graphml_generate----------------
        GF.graphml_generate(graph[0], graph[1], 'merged_mark.graphml', debug_flag=False)

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

