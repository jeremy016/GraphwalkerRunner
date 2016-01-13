#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import requests,json,os,sys,time,traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xml.etree.cElementTree as ET
import urllib2
import ConfigParser

global driver,wait

def setConfig(section, option, value):
	cfg_path = '/home/tonychang/sikulixrunserver/Justup/Config/justup.cfg'
	cfg = ConfigParser.ConfigParser()
	#cfg = ConfigParser.RawConfigParser()
	cfg.read(cfg_path)
	cfg.set(section, option, value)
	cfg.write(open(cfg_path, "w",0))
	
def e_ClickSettings() :
    global driver,wait, remote_server_flag
    print( "e_ClickSettings" )

    #element = wait.until(EC.element_to_be_clickable((By.ID,'user-avatar')))
    #time.sleep(1)
    #avatar_img = driver.find_element_by_id("user-avatar").click()

    try:
        if remote_server_flag == True:
		urllib2.urlopen('http://localhost:50001/run/click_setting')
	else:
        	os.popen("java -jar /home/tonychang/sikulixrunserver/sikulix.jar -r /home/tonychang/sikulixrunserver/Justup/click_setting.sikuli")
    except Exception as e:
    	None

    return 1

def e_CloseWindows() :
    global driver,wait
    print( "e_CloseWindows" )

    driver.get('https://justup.9ifriend.com/')

    return 1

def e_Login() :
    global driver,wait, remote_server_flag
    print( "e_Login" )
  
    #try:

    #    submit_button = driver.find_element_by_id('just-login').click()
    #    element = wait.until(EC.element_to_be_clickable((By.ID,'uemail')))
        
    #except:

    #    print 'pass'

    try:
        if remote_server_flag == True:
		urllib2.urlopen('http://localhost:50001/run/login')
	else:
        	os.popen("java -jar /home/tonychang/sikulixrunserver/sikulix.jar -r /home/tonychang/sikulixrunserver/Justup/login.sikuli")
    except Exception as e:
    	None

    return 1


def e_LoginFail_FailPassword() :
    global driver,wait, remote_server_flag
    print( "e_LoginFail_FailPassword" )

    #element = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))

    #uemail = driver.find_element_by_id("uemail")
    #uemail.clear()
    #uemail.send_keys(Keys.NULL)
    #uemail.send_keys('lumy')

    #upasswd = driver.find_element_by_id("upasswd")
    #upasswd.clear()
    #upasswd.send_keys('123456')

    #submit_button = driver.find_element_by_id('login-button').click()

    #element = wait.until(EC.element_to_be_clickable((By.ID,'alertContent')))

    #time.sleep(1)
    try:
        if remote_server_flag == True:
		#urllib2.urlopen('http://localhost:50001/run/login_failpwd')
		setConfig('LOGIN','f_email','lumy')
		setConfig('LOGIN','f_pwd','123456')
		urllib2.urlopen('http://localhost:50001/run/login_fail')
	else:
        	os.popen("java -jar /home/tonychang/sikulixrunserver/sikulix.jar -r /home/tonychang/sikulixrunserver/Justup/login_failpwd.sikuli")
    except Exception as e:
    	None
    
    #uni_str = driver.find_element_by_id("alertContent").text
    #assert unicode(uni_str) == u'登入失敗！請重新輸入電子郵件與密碼。'
    #assert unicode(uni_str) == u'登入失敗！請重新輸入帳號/電子郵件, 與密碼。'

    return 1

def e_LoginFail_NonePassword() :
    global driver,wait, remote_server_flag
    print( "e_LoginFail_NonePassword" )

    #element = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))

    #uemail = driver.find_element_by_id("uemail")
    #uemail.clear()
    #uemail.send_keys(Keys.NULL)
    #uemail.send_keys('lumy')

    #upasswd = driver.find_element_by_id("upasswd")
    #upasswd.clear()
    #upasswd.send_keys('')

    #submit_button = driver.find_element_by_id('login-button').click()


    #element = wait.until(EC.element_to_be_clickable((By.ID,'alertContent')))

    try:
        if remote_server_flag == True:
		setConfig('LOGIN','f_email','lumy')
		setConfig('LOGIN','f_pwd','')
		urllib2.urlopen('http://localhost:50001/run/login_fail')
		#urllib2.urlopen('http://localhost:50001/run/login_nopwd')
	else:
        	os.popen("java -jar /home/tonychang/sikulixrunserver/sikulix.jar -r /home/tonychang/sikulixrunserver/Justup/login_nopwd.sikuli")
    except Exception as e:
    	None
    
    time.sleep(1)

    uni_str = driver.find_element_by_id("alertContent").text
    
    assert unicode(uni_str) == u'請填寫您的密碼。'
    return 1

def e_LoginFail_NullAccountPassword() :
    global driver,wait, remote_server_flag
    print( "e_LoginFail_NullAccountPassword" )

    #element = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))

    #uemail = driver.find_element_by_id("uemail")
    #uemail.clear()
    #uemail.send_keys(Keys.NULL)
    #uemail.send_keys('')

    #upasswd = driver.find_element_by_id("upasswd")
    #upasswd.clear()
    #upasswd.send_keys('')

    #submit_button = driver.find_element_by_id('login-button').click()

    #element = wait.until(EC.element_to_be_clickable((By.ID,'alertContent')))

    try:
        if remote_server_flag == True:
		setConfig('LOGIN','f_email','')
		setConfig('LOGIN','f_pwd','')
		urllib2.urlopen('http://localhost:50001/run/login_fail')
		#urllib2.urlopen('http://localhost:50001/run/login_noacpwd')
	else:
        	os.popen("java -jar /home/tonychang/sikulixrunserver/sikulix.jar -r /home/tonychang/sikulixrunserver/Justup/login_noacpwd.sikuli")
    except Exception as e:
    	None

    time.sleep(1)

    uni_str = driver.find_element_by_id("alertContent").text

    #assert unicode(uni_str) == u'請填寫您的帳號或電子郵件'
    assert unicode(uni_str) == u'請填寫您的帳號或電子郵件。'
    
    return 1

def e_LoginPass() :
    global driver,wait, remote_server_flag
    print( "e_LoginPass" )

    #element = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))

    #uemail = driver.find_element_by_id("uemail")
    #uemail.clear()
    #uemail.send_keys(Keys.NULL)
    #uemail.send_keys('lumy')

    #upasswd = driver.find_element_by_id("upasswd")
    #upasswd.clear()
    #upasswd.send_keys('Aa123456')

    #submit_button = driver.find_element_by_id('login-button').click()

    try:
        if remote_server_flag == True:
		setConfig('LOGIN','f_email','lumy')
		setConfig('LOGIN','f_pwd','Aa123456')
		urllib2.urlopen('http://localhost:50001/run/login_fail')
		#urllib2.urlopen('http://localhost:50001/run/login_success')
	else:
        	os.popen("java -jar /home/tonychang/sikulixrunserver/sikulix.jar -r /home/tonychang/sikulixrunserver/Justup/login_success.sikuli")
    except Exception as e:
    	None
    
    return 1

def e_Logout() :
    global driver,wait
    print( "e_Logout" )

    #submit_button = driver.find_element_by_id('log-out').click()

    #element = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))

    try:
        if remote_server_flag == True:
		urllib2.urlopen('http://localhost:50001/run/logout')
	else:
        	os.popen("java -jar /home/tonychang/sikulixrunserver/sikulix.jar -r /home/tonychang/sikulixrunserver/Justup/logout.sikuli")
    except Exception as e:
    	None

    return 1


def e_init() :
    global driver,wait, remote_server_flag

    print( "e_init" )

    params = {}
    if sys.argv[1]  != '':
	params['browserName'] = sys.argv[1] 
    if sys.argv[2]  != '':
	params['platform'] = sys.argv[2] 
    if sys.argv[3]  != '':
	params['version'] = sys.argv[3] 
    
    remote_server_flag = True
    if sys.argv[4]  != '':
	remote_server_flag = False	

    print params
    #driver = webdriver.Chrome()
    driver = webdriver.Remote(
               command_executor = 'http://localhost:7777/wd/hub',
	       #command_executor = 'http://10.62.44.69:7777/wd/hub',
               desired_capabilities = params)

    #get selenium  node ip and port begin
    #sessionId = self.driver.desired_capabilities['webdriver.remote.sessionid']

    #response = urllib2.urlopen('http://192.168.20.140:7777/grid/api/testsession?session=' + sessionId)
    #node_ip_port = json.loads(response.read())['proxyId'].rsplit(":",1)
    #sikuli_ip_port = [node_ip_port[0], int(node_ip_port[1])+1]
    #print sikuli_ip_port
    #get selenium  node ip and port end
    
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

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

    #element = wait.until(EC.element_to_be_clickable((By.ID,'log-out2')))
    element = wait.until(EC.element_to_be_clickable((By.ID,'log-out')))

    return 


gw_url = 'http://localhost:8887/graphwalker'


step_list=[]

Test_result = 'Pass'

while requests.get(gw_url+'/hasNext').json()['HasNext'] == 'true' :
    # Get next step from GraphWalker
    step = requests.get(gw_url+'/getNext').json()['CurrentElementName']
    step_list.append(step)
    if step != '' :
        #eval( step + "()" )

        try:
            eval( step + "()" )

        except Exception as e:
            Test_result='Fail'
            Exception_msg=traceback.format_exc()
            break

#Generate XML
#testsuite = ET.Element("testsuite", TestCount=str(len(step_list)), TestResult=Test_result)
    
#if Test_result == 'Fail':
#    ET.SubElement(testsuite,"error" ,name='erroe_message').text = str(Exception_msg)

#tree = ET.ElementTree(testsuite)


#tree.write("Result.xml", 'UTF-8', 'True')
driver.close()
