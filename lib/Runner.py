
# -*- coding: utf-8 -*-
import requests,json,traceback,time,sys,os,imp
import GraphFun as GraphFun
# import script as RunFun

from subprocess import Popen, PIPE
import logging
import logging.config

global temp
temp={}


RunFun = imp.load_source('script', sys.argv[1]+'/script.py')







#init parameter
NoneError = True
Pid_exist = True
blocked_exist = True
error_list = []
pass_dic = {}
BLOCKED = {}

##########Set log################

logging.config.fileConfig("/usr/local/GraphwalkerRunner/logger.conf")
logger = logging.getLogger("example01")

#################################

#creat GraphFun object----------------


try:

#creat "GraphFun" object
    GF = GraphFun.GraphFun()

#cp merged.graphml to too's lib
    p = Popen(['cp','merged.graphml','/usr/local/GraphwalkerRunner/lib/merged_mark.graphml'],stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
    output, error = p.communicate()
    if p.returncode == 0:
        ok=False if output else True        
    else:
        ok=False
    assert ok==True,error

#Get average count
    logger.info('Get average count...')
    Max,Min,Stop = GF.Stop_Condition(sys.argv[1])

    test_count=0

    argv_3 = sys.argv[3] if sys.argv[3] != 'False' else False
    argv_4 = True if sys.argv[4] != 'False' else False
    
    if argv_3:

        if not os.path.exists(sys.argv[1]+'/Screenshot'):
            os.popen('mkdir '+sys.argv[1]+'/Screenshot')
        else:
            os.popen("rm -rf "+sys.argv[1]+"/Screenshot")
            os.popen('mkdir '+sys.argv[1]+'/Screenshot')

#start running GW
    os.popen('adb ' + serial + ' shell logcat -c')           
  
    while(NoneError):
        step_count=0

        if test_count==0:
            command =  'The_'+str(test_count+1)+'st_times_testing'
        elif test_count==1:
            command =  'The_'+str(test_count+1)+'nd_times_testing'
        elif test_count==2:
            command =  'The_'+str(test_count+1)+'rd_times_testing'
        else:
            command =  'The_'+str(test_count+1)+'th_times_testing'

        if argv_3:
            
            p = Popen(['mkdir',sys.argv[1]+'/Screenshot/'+str(command)],stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
            output, error = p.communicate()
            if p.returncode == 0:
                ok=False if output else True        
            else:
                ok=False
            assert ok==True,error
        
        test_count+=1

        print '\nRun Testing...\n'
        GF.kill_Process() 

        GF.Run_Websocket(sys.argv[2])  

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
                    logger.debug('[CurrentElementName error] : '+str(e))
                    # BLOCKED Error Handling 
                    BLOCKED,Stop,NoneError,Test_result = GF.BLOCKED_Exception_Action('getNext', e, BLOCKED, Max, Min, step, NoneError,Test_result)
                    break

                step_list.append(str(step))

                #Run Function
                if step != '' :
                    try:
                        eval( "RunFun."+step + "()" )
                        Stop-=1

                        GF.screen_shot(argv_3,sys.argv[1],command,str(step_count),step)
            
                        step_count+=1

                    #Fun error
                    except Exception as e:
                        #Fun error Handling
                        Stop,NoneError,Test_result,error_list = GF.Fun_Exception_Action(e, Max, Min, step, NoneError,Test_result,step_list,error_list,sys.argv[1],argv_4)
                        logger.debug('[Function error] : '+str(Test_result))
                     
                        break

            #integrate screen capture code to templete
            GF.screen_shot(argv_3,sys.argv[1],command,str(step_count),step)

        # Step(HasNext) occured error
        except Exception as e:
            logger.debug('[HasNext error] : '+str(e))
            #occured Connection aborted error
            if  'Connection refused' in str(e):
                
                root_cause,step = GF.Connection_Aborted(e,sys.argv[2])

                logger.debug('[Connection refused] root_cause : '+str(root_cause)+' ; step : '+str(step))

                if 'No start context found' == str(root_cause):
                    logger.debug('No start context found')
                    break
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


       

    print ('*********************')
    print (str(complete_value))
    print ('*********************')

    print ('*********************')
    print (str(BLOCKED))
    print ('*********************')


    #Generate Test Report
    GF.Test_Report(complete_value, error_list,pass_dic,BLOCKED)
    #Generate XML
    GF.Generate_XML(complete_value, error_list,pass_dic,BLOCKED)

    #kill service
    GF.kill_Process('Graphwalker_Runner')


except KeyboardInterrupt as e:
    logger.error('KeyboardInterrupt')
    self.kill_Process('Runner.py')

except Exception, e:

    logger.error(str(e))

