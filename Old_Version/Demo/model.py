#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import requests,json,os,sys,time,traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xml.etree.cElementTree as ET

global driver,wait



def e_ClickSettings() :
    global driver,wait
    print( "e_ClickSettings" )

    element = wait.until(EC.element_to_be_clickable((By.ID,'user-avatar')))
    time.sleep(1)
    avatar_img = driver.find_element_by_id("user-avatar").click()


    return 1




def e_CloseWindows() :
    global driver,wait
    print( "e_CloseWindows" )

    driver.get('https://justup.9ifriend.com/')

    return 1




def e_Login() :
    global driver,wait
    print( "e_Login" )
  
    try:

        submit_button = driver.find_element_by_id('just-login').click()
        
        
        element = wait.until(EC.element_to_be_clickable((By.ID,'uemail')))

    except:

        print 'pass'

    return 1


def e_LoginFail_FailPassword() :
    global driver,wait
    print( "e_LoginFail_FailPassword" )

    element = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))

    uemail = driver.find_element_by_id("uemail")
    uemail.clear()
    uemail.send_keys(Keys.NULL)
    uemail.send_keys('lumy')

    upasswd = driver.find_element_by_id("upasswd")
    upasswd.clear()
    upasswd.send_keys('123456')

    submit_button = driver.find_element_by_id('login-button').click()

    element = wait.until(EC.element_to_be_clickable((By.ID,'alertContent')))

    time.sleep(1)
    
    uni_str = driver.find_element_by_id("alertContent").text
    
    assert unicode(uni_str) == u'登入失敗！請重新輸入電子郵件與密碼。'


    return 1




def e_LoginFail_NonePassword() :
    global driver,wait
    print( "e_LoginFail_NonePassword" )

    element = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))

    uemail = driver.find_element_by_id("uemail")
    uemail.clear()
    uemail.send_keys(Keys.NULL)
    uemail.send_keys('lumy')

    upasswd = driver.find_element_by_id("upasswd")
    upasswd.clear()
    upasswd.send_keys('')

    submit_button = driver.find_element_by_id('login-button').click()


    element = wait.until(EC.element_to_be_clickable((By.ID,'alertContent')))

    time.sleep(1)

    uni_str = driver.find_element_by_id("alertContent").text

    assert unicode(uni_str) == u'請填寫您的密碼。'


    return 1




def e_LoginFail_NullAccountPassword() :
    global driver,wait
    print( "e_LoginFail_NullAccountPassword" )

    element = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))

    uemail = driver.find_element_by_id("uemail")
    uemail.clear()
    uemail.send_keys(Keys.NULL)
    uemail.send_keys('')

    upasswd = driver.find_element_by_id("upasswd")
    upasswd.clear()
    upasswd.send_keys('')

    submit_button = driver.find_element_by_id('login-button').click()

    element = wait.until(EC.element_to_be_clickable((By.ID,'alertContent')))

    time.sleep(1)

    uni_str = driver.find_element_by_id("alertContent").text
    
    #assert unicode(uni_str) == u'請填寫您的帳號或電子郵件'
    assert unicode(uni_str) == u'請填寫您的帳號或電子郵件。'


    return 1




def e_LoginPass() :
    global driver,wait
    print( "e_LoginPass" )

    element = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))

    uemail = driver.find_element_by_id("uemail")
    uemail.clear()
    uemail.send_keys(Keys.NULL)
    uemail.send_keys('lumy')

    upasswd = driver.find_element_by_id("upasswd")
    upasswd.clear()
    upasswd.send_keys('Aa123456')

    submit_button = driver.find_element_by_id('login-button').click()

    return 1




def e_Logout() :
    global driver,wait
    print( "e_Logout" )

    submit_button = driver.find_element_by_id('log-out').click()

    element = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))

    return 1




def e_init() :
    global driver,wait

    print( "e_init" )

    params = {}
    if sys.argv[1]  != '':
        params['browserName'] = sys.argv[1] 
    if sys.argv[2]  != '':
        params['platform'] = sys.argv[2] 
    if sys.argv[3]  != '':
        params['version'] = sys.argv[3] 


    #driver = webdriver.Chrome()
    driver = webdriver.Remote(
               command_executor = 'http://localhost:7777/wd/hub',
               desired_capabilities = params)    
    wait = WebDriverWait(driver, 10)
    #driver.maximize_window()

    return 1




def v_JustupMainPage() :
    global driver,wait
     
    print( "v_JustupMainPage" )

    element = wait.until(EC.element_to_be_clickable((By.ID,'logo')))

    return 1




def v_LoginPage() :
    global driver,wait

    print( "v_LoginPage" )

    element = wait.until(EC.element_to_be_clickable((By.ID,'login-input-account')))

    return 1

    


def v_OpenClient() :
    global driver,wait
    print( "v_OpenClient" )


    driver.get('https://justup.9ifriend.com/')


    return 1




def v_SettingList() :
    global driver,wait

    print( "v_SettingList" )

    element = wait.until(EC.element_to_be_clickable((By.ID,'log-out2')))



    return 


gw_url = 'http://localhost:8887/graphwalker'

step_list=[]

Test_result = {}

while requests.get(gw_url+'/hasNext').json()['HasNext'] == 'true' :
    # Get next step from GraphWalker
    step = requests.get(gw_url+'/getNext').json()['CurrentElementName']
    step_list.append(str(step))
    if step != '' :
        try:
            eval( step + "()" )
            Test_result[step] = 'Pass'
        except Exception as e:
            print e
            Test_result[step] = 'Fail'
            exc_type, exc_value, exc_traceback = sys.exc_info()
            break
    
#Generate XML

testsuite = ET.Element("testsuite", Tests=str(len(step_list)))

properties = ET.SubElement(testsuite,"properties")

step_str = '->'.join(step_list)

print 'step_str:'
print step_str

index = 0
for i in step_list:
    index+=1
    index_str = str(index)
    zfill = index_str.zfill(4)

    testcase = ET.SubElement(testsuite,"testcase" ,classname='model',name=zfill+'_'+str(i))

    if Test_result[i] == 'Fail':
        message_str='The Step :\n '+str(step_str)+ '\nerror message:\n+exc_type:' +str(exc_type)+'\nexc_value:'+str(exc_value)+'\nexc_traceback:'+str(exc_traceback)+'\n'
        ET.SubElement(testcase,"error" ,message=str(message_str), type=str(exc_type)).text =str(sys.exc_info())

    if Test_result[i] == 'Pass':

        ET.SubElement(testcase,"Pass" ,message='The Step :\n '+str(step_str))


tree = ET.ElementTree(testsuite)


tree.write("Result.xml", 'UTF-8', 'True')


f = open('json.json','w')

f.write(json.dumps(step_list))

f.close()

driver.close()