# -*- coding: utf-8 -*- 
import requests,json,traceback,time,sys,os
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import lib.selenium_lib as SL

global temp
temp={}

print "System default encoding: " + sys.getdefaultencoding()  
reload(sys)  
sys.setdefaultencoding('utf8')


def e_Init() :
    print "e_Init"
    global temp
     
    capabilities = {
      'chromeOptions': {
        'androidPackage': 'com.android.chrome',
        "args": ["--disable-translate","--incognito"]
      }
    }

    temp['driver'] = webdriver.Remote('http://localhost:9515', capabilities)
    temp['wait'] = WebDriverWait(temp['driver'], 10)
    temp['driver'].get('https://justup.9ifriend.com/')

    # README
    # Landing/Login use system default but main page use server default.
    # QA needs to align test account locale & system locale before test
    userLanguage = temp['driver'].execute_script("return window.navigator.userLanguage || window.navigator.language ;")
    print "userLanguage: " + userLanguage
    json_data=open('resource.json').read()
    data = json.loads(json_data)
    temp['resource'] = data[userLanguage]

    return "e_Init"



def e_Valid_Login() :
    print "e_Valid_Login"
    global temp

    temp['driver'].find_element_by_id("uemail").clear()
    temp['driver'].find_element_by_id("uemail").send_keys("hh.idbg.test@gmail.com")
    temp['driver'].find_element_by_id("upasswd").clear()
    temp['driver'].find_element_by_id("upasswd").send_keys("hh888888")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'login-button')))
    temp['driver'].find_element_by_id("login-button").click()    
     
    return "e_Valid_Login"



def e_btn_About() :
    print "e_btn_About (from Login to v_Landing_Page, actully new tab)"
    global temp

    temp['driver'].find_element_by_xpath("//table[@id='login-right-link']/tbody/tr/td[1]").click()
     
    if len(temp['driver'].window_handles) > 1:

        window_before = temp['driver'].window_handles[-2]
        window_after = temp['driver'].window_handles[-1]

        temp['driver'].close()
        temp['driver'].switch_to_window(window_after)
        # temp['driver'].find_element_by_class_name('forget-form-body')

    return "e_btn_About"



def e_btn_Back() :
    print "e_btn_Back"
    global temp

    temp['driver'].find_element_by_id('return-more-menu').click()
     
    return "e_btn_Back"



def e_btn_Download() :
    print "e_btn_Download"
    global temp

    temp['driver'].find_element_by_id('just-download').click()     
    return "e_btn_Download"



def e_btn_Login() :
    global temp
    print( "e_btn_Login" )

    temp['driver'].find_element_by_id('just-login').click()

    return


def e_btn_Register() :
    global temp
    print( "e_btn_Register" )

    temp['driver'].find_element_by_id('btn-register').click()

    return



def e_img_Favorite() :
    print "e_img_Favorite"
    global temp

    temp['driver'].find_element_by_id('footer-btn-my-favorite').click()
    return "e_img_Favorite"



def e_img_Filelist() :
    print "e_img_Filelist"
    global temp

    temp['driver'].find_element_by_id('footer-btn-all-files').click()
     
    return "e_img_Filelist"


def e_img_More() :
    print "e_img_More"
    global temp

    temp['driver'].find_element_by_id('footer-btn-more').click()
     
    return "e_img_More"



def e_img_Share() :
    print "e_img_Share"
    global temp

    temp['driver'].find_element_by_id('footer-btn-share').click()
     
    return "e_img_Share"



def e_img_Trash_Bin() :
    print "e_img_Trash_Bin"
    global temp

    temp['driver'].find_element_by_id('footer-btn-trash').click()
     
    return "e_img_Trash_Bin"




def e_link_Signup() :
    print "e_link_Signup"
    global temp

    temp['driver'].find_element_by_id('just-signup').click()
     
    return "e_link_Signup"



def e_link_Register() :
    print "e_link_Register"
    global temp

    temp['driver'].find_element_by_id('login-register').click()
     
    return "e_link_Register"


def e_link_Forgot_Password() :
    print "e_link_Forgot_Password"
    global temp

    temp['driver'].find_element_by_id('login-forget').click()
     
    return "e_link_Forgot_Password"



def e_link_Notification() :
    print "e_link_Notification"
    global temp
    
    temp['driver'].find_element_by_id('more-active').click() 
    return "e_link_Notification"



def e_link_System_Bulletin() :
    print "e_link_System_Bulletin"
    global temp
     
    temp['driver'].find_element_by_id('more-admin').click() 
    return "e_link_System_Bulletin"



def e_logout() :
    print "e_logout"
    global temp

    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight);")
    temp['driver'].find_element_by_id('more-logout').click() 
     
    return "e_logout"


def e_img_Home_to_Login():
    global temp
    print( "e_img_Home_to_Login" )

    temp['driver'].find_elements_by_class_name('home-logo')[0].click()

    return "e_img_Home_to_Login"


def v_Download_Page() :
    print "v_Download_Page"
    global temp

    temp['driver'].find_element_by_id('download-hero').click() 
     
    return "v_Download_Page"



def v_Favorite() :
    print "v_Favorite"
    global temp
     
    temp['driver'].find_element_by_xpath("//font[contains(text(),temp['resource']['footer-btn-text-favorite'])]")

    return "v_Favorite"



def v_Forget_Password_Page() :
    print "v_Forget_Password_Page"
    global temp

    

    if len(temp['driver'].window_handles) > 1:

        window_before = temp['driver'].window_handles[-2]
        window_after = temp['driver'].window_handles[-1]

        temp['driver'].close()
        temp['driver'].switch_to_window(window_after)
        # temp['driver'].maximize_window()
        temp['driver'].find_element_by_class_name('forget-form-body')
     
    return "v_Forget_Password_Page"



def v_Landing_Page() :
    global temp
    print( "v_LandingPage" )

    time.sleep(1)

    temp['driver'].find_element_by_id('section-hero')

    return



def v_Login_Page() :
    global temp
    print( "v_LoginPage" )


    temp['wait'].until(EC.element_to_be_clickable((By.ID,'userLogin')))
    time.sleep(2)
    RegisterPage = temp['driver'].find_element_by_id('userLogin')

    assert(type(RegisterPage).__name__=='WebElement')

    return



def v_Main_Page() :
    print "v_Main_Page"
    global temp

    # TODO: replace static wait of object-existing waiting
    time.sleep(5)
    temp['driver'].find_element_by_xpath("//font[contains(text(),temp['resource']['footer-btn-text-files'])]")
     
    return "v_Main_Page"



def v_More_Actions() :
    print "v_More_Actions"
    global temp

    temp['driver'].find_element_by_xpath("//font[contains(text(),temp['resource']['footer-btn-text-more'])]")
     
    return "v_More_Actions"



def v_Notification() :
    print "v_Notification"
    global temp

    temp['driver'].find_element_by_xpath("//font[contains(text(),temp['resource']['footer-btn-text-act-note'])]")
     
    return "v_Notification"



def v_Register_Page() :
    print "v_Register_Page"
    global temp
     
    return "v_Register_Page"



def v_Shared_Items() :
    print "v_Shared_Items"
    global temp

    temp['driver'].find_element_by_xpath("//font[contains(text(),temp['resource']['footer-btn-text-share'])]")
     
    return "v_Shared_Items"



def v_System_Bulletin() :
    print "v_System_Bulletin"
    global temp

    temp['driver'].find_element_by_xpath("//font[contains(text(),temp['resource']['footer-btn-text-admin-note'])]")
     
    return "v_System_Bulletin"



def v_Trash_Bin() :
    print "v_Trash_Bin"
    global temp

    temp['driver'].find_element_by_xpath("//font[contains(text(),temp['resource']['footer-btn-text-trash'])]")
     
    return "v_Trash_Bin"
