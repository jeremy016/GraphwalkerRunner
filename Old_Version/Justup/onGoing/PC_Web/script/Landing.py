# -*- coding: utf-8 -*-
import requests,json,traceback,time,sys
import xml.etree.cElementTree as ET

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

global temp
temp={}

def e_init() :
    global temp

    print( "e_init" )
    
    temp['driver'] = webdriver.Firefox()
    temp['action'] = webdriver.ActionChains(temp['driver'])
    temp['wait'] = WebDriverWait(temp['driver'], 10)
    temp['driver'].maximize_window()

    temp['driver'].get('https://justup.9ifriend.com/')

    #get userLanguage
    userLanguage = temp['driver'].execute_script("return window.navigator.userLanguage || window.navigator.language ;")
    json_data=open('lib/Language.json').read()
    data = json.loads(json_data)
    temp['Language'] = data[userLanguage]
 
    return


def v_LandingPage() :
    global temp
    print( "v_LandingPage" )

    time.sleep(1)

    temp['driver'].find_element_by_id('section-hero')

    return

def e_btn_UploadClassify() :
    global temp
    print( "e_btn_UploadClassify" )

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'features-01')))

    temp['driver'].find_element_by_id('features-01').click()

    element_position = temp['driver'].execute_script("return document.getElementById('section-feature-classify').offsetTop")
    
    scrollTop = temp['driver'].execute_script("return document.documentElement.scrollTop")

    assert (element_position==scrollTop)

    submit_button = temp['driver'].find_element_by_id('justop').click()
    time.sleep(1)
    return

def e_btn_RealTimeBrowse() :
    global temp
    print( "e_btn_RealTimeBrowse" )

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'features-02')))

    temp['driver'].find_element_by_id('features-02').click()

    element_position = temp['driver'].execute_script("return document.getElementById('section-feature-access').offsetTop")
    
    scrollTop = temp['driver'].execute_script("return document.documentElement.scrollTop")

    assert (element_position==scrollTop)

    submit_button = temp['driver'].find_element_by_id('justop').click()
    time.sleep(1)
    return

def e_btn_Collaborate() :
    global temp
    print( "e_btn_Collaborate" )
  
    temp['wait'].until(EC.element_to_be_clickable((By.ID,'features-03')))

    temp['driver'].find_element_by_id('features-03').click()

    element_position = temp['driver'].execute_script("return document.getElementById('section-feature-collaborate').offsetTop")
    
    scrollTop = temp['driver'].execute_script("return document.documentElement.scrollTop")

    submit_button = temp['driver'].find_element_by_id('justop').click()

    time.sleep(1)

    return


def e_btn_Top() :
    global temp
    print( "e_btn_Top" )

    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

    submit_button = temp['driver'].find_element_by_id('justop').click()

    time.sleep(1)

    Current_Height = temp['driver'].execute_script("return document.documentElement.scrollTop")
   
    assert (Current_Height==0)

    return

def e_btn_ShowDocPng() :
    global temp
    print( "e_btn_ShowDocPng" )

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'features-02')))

    temp['driver'].find_element_by_id('features-02').click()

    temp['driver'].find_element_by_id('feature_access_tab1').click()

    display = temp['driver'].find_elements_by_xpath('//div[@id="feature_access_01"]//img[@src]')[0].get_attribute('style').split(';')[0].split(':')

    if display[0]!='opacity':

        time.sleep(1)

        temp['driver'].find_element_by_id('feature_access_tab1').click()

        display = temp['driver'].find_elements_by_xpath('//div[@id="feature_access_01"]//img[@src]')[0].get_attribute('style').split(';')[0].split(':')        

    # assert (display[0]=='opacity' or display[1]==' inline')

    submit_button = temp['driver'].find_element_by_id('justop').click()
    
    time.sleep(1)

    return




def e_btn_ShowImagePng() :
    global temp
    print( "e_btn_ShowImagePng" )

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'features-02')))

    temp['driver'].find_element_by_id('features-02').click()

    temp['driver'].find_element_by_id('feature_access_tab2').click()

    display = temp['driver'].find_elements_by_xpath('//div[@id="feature_access_02"]//img[@src]')[0].get_attribute('style').split(';')[0].split(':')

    if display[0]!='opacity':

        time.sleep(1)

        temp['driver'].find_element_by_id('feature_access_tab2').click()

        display = temp['driver'].find_elements_by_xpath('//div[@id="feature_access_02"]//img[@src]')[0].get_attribute('style').split(';')[0].split(':')        

    # assert (display[0]=='opacity' or display[1]==' inline')

    submit_button = temp['driver'].find_element_by_id('justop').click()
    
    time.sleep(1)

    return




def e_btn_ShowMusicPng() :
    global temp
    print( "e_btn_ShowMusicPng" )


    temp['wait'].until(EC.element_to_be_clickable((By.ID,'features-02')))

    temp['driver'].find_element_by_id('features-02').click()

    temp['driver'].find_element_by_id('feature_access_tab3').click()

    display = temp['driver'].find_elements_by_xpath('//div[@id="feature_access_03"]//img[@src]')[0].get_attribute('style').split(';')[0].split(':')

    if display[0]!='opacity':

        time.sleep(1)

        temp['driver'].find_element_by_id('feature_access_tab3').click()

        display = temp['driver'].find_elements_by_xpath('//div[@id="feature_access_03"]//img[@src]')[0].get_attribute('style').split(';')[0].split(':')        

    # assert (display[0]=='opacity' or display[1]==' inline')

    submit_button = temp['driver'].find_element_by_id('justop').click()
    
    time.sleep(1)
    return




def e_btn_ShowVideoPng() :
    global temp
    print( "e_btn_ShowVideoPng" )


    temp['wait'].until(EC.element_to_be_clickable((By.ID,'features-02')))

    temp['driver'].find_element_by_id('features-02').click()

    temp['driver'].find_element_by_id('feature_access_tab4').click()

    display = temp['driver'].find_elements_by_xpath('//div[@id="feature_access_04"]//img[@src]')[0].get_attribute('style').split(';')[0].split(':')

    if display[0]!='opacity':

        time.sleep(1)

        temp['driver'].find_element_by_id('feature_access_tab4').click()

        display = temp['driver'].find_elements_by_xpath('//div[@id="feature_access_04"]//img[@src]')[0].get_attribute('style').split(';')[0].split(':')        

    # assert (display[0]=='opacity' or display[1]==' inline')

    submit_button = temp['driver'].find_element_by_id('justop').click()
    
    time.sleep(1)
    return

def e_footer_Blog() :
    global temp
    print( "e_footer_Blog" )
    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight);")
   
    temp['driver'].find_elements_by_xpath("//div[@id='just-wrap']/footer/div/ul/li[3]")[0].click()
    return




def e_footer_FB() :
    global temp
    print( "e_footer_FB" )

    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight);")
   
    temp['driver'].find_elements_by_xpath("//div[@id='just-wrap']/footer/div/ul/li[6]/a[2]/img")[0].click()

    return




def e_footer_GooglePlus() :
    global temp
    print( "e_footer_GooglePlus" )

    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight);")
   
    temp['driver'].find_elements_by_xpath("//div[@id='just-wrap']/footer/div/ul/li[6]/a[3]/img")[0].click()

    return




def e_footer_PrivacyPolicy() :
    global temp
    print( "e_footer_PrivacyPolicy" )

    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight);")
   
    temp['driver'].find_elements_by_xpath("//div[@id='just-wrap']/footer/div/ul/li[5]")[0].click()
    return




def e_footer_ServicePolicy() :
    global temp
    print( "e_footer_ServicePolicy" )

    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight);")
   
    temp['driver'].find_elements_by_xpath("//div[@id='just-wrap']/footer/div/ul/li[4]")[0].click()

    return




def e_footer_Twitter() :
    global temp
    print( "e_footer_Twitter" )

    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    temp['driver'].find_elements_by_xpath("//div[@id='just-wrap']/footer/div/ul/li[6]/a/img")[0].click()

    
    return

def e_Landing_close_tab() :
    global temp
    print( "e_Landing_close_tab" )
    
    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]

    temp['driver'].close()
    temp['driver'].switch_to_window(window_before)
    current_url = temp['driver'].current_url

    return

def v_Landing_TwitterPage() :
    global temp
    print( "v_Landing_TwitterPage" )

    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]
    temp['driver'].switch_to_window(window_after)
    current_url = temp['driver'].current_url
    assert(current_url=='https://twitter.com/JustupService')

    return

def v_Landing_ServicePolicyPage() :
    global temp
    print( "v_Landing_ServicePolicyPage" )

    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]
    temp['driver'].switch_to_window(window_after)

    current_url = temp['driver'].current_url
    assert(current_url=='http://web.9ifriend.com/drive/policy.html')

    return

def v_Landing_GooglePlusPage() :
    global temp
    print( "v_Landing_GooglePlusPage" )

    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]
    temp['driver'].switch_to_window(window_after)

    current_url = temp['driver'].current_url
    assert(current_url=='https://plus.google.com/+JustupCloud')

    return

def v_Landing_FBPage() :
    global temp
    print( "v_Landing_FBPage" )
    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]
    temp['driver'].switch_to_window(window_after)

    current_url = temp['driver'].current_url
    assert(current_url=='https://www.facebook.com/Justupcloud/')
    return

def v_Landing_PrivacyPolicyPage() :
    global temp
    print( "v_Landing_PrivacyPolicyPage" )
    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]
    temp['driver'].switch_to_window(window_after)

    current_url = temp['driver'].current_url
    assert(current_url=='http://web.9ifriend.com/policies/index.html')
    return

def v_Landing_BlogPage() :
    global temp
    print( "v_BlogPage" )
    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]
    temp['driver'].switch_to_window(window_after)

    current_url = temp['driver'].current_url
    assert(current_url=='https://blog.justup.co/')
    return


def e_btn_FreeRegister() :
    global temp
    print( "e_btn_FreeRegister" )

    temp['driver'].find_element_by_id('btn-register').click()


    return

def e_btn_JustupSignup() :
    global temp
    print( "e_btn_JustupSignup" )

    just_top = temp['driver'].find_elements_by_class_name("just-top")

    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    
    time.sleep(1)

    just_top = temp['driver'].find_elements_by_class_name("just-top")

    assert(type(just_top[0]).__name__=='WebElement')
    
    temp['driver'].find_element_by_id('just-signup').click()

    return

def e_btn_GetFreeSpace() :
    global temp
    print( "e_btn_GetFreeSpace" )

    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight);")

    temp['driver'].find_element_by_id('btn-ending-call').click()

    return

def v_RegisterPage() :
    global temp
    print( "v_RegisterPage" )

    time.sleep(1)

    RegisterPage = temp['driver'].find_element_by_id('userRegister')

    assert(type(RegisterPage).__name__=='WebElement')

    return

def e_Register_icon_HomeLogo() :
    global temp
    print( "e_icon_HomeLogo" )

    temp['driver'].find_elements_by_class_name('home-logo')[0].click()

    return

def e_btn_Login() :
    global temp
    print( "e_btn_Login" )

    temp['driver'].find_element_by_id('just-login').click()

    return

def v_LoginPage() :
    global temp
    print( "v_LoginPage" )


    temp['wait'].until(EC.element_to_be_clickable((By.ID,'userLogin')))
    time.sleep(2)
    RegisterPage = temp['driver'].find_element_by_id('userLogin')

    assert(type(RegisterPage).__name__=='WebElement')

    return

def e_Login_btn_ContactUs() :
    global temp
    print( "e_Login_btn_ContactUs" )

    temp['driver'].find_element_by_xpath("//table[@id='login-right-link']/tbody/tr/td").click()

    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]

    temp['driver'].close()
    temp['driver'].switch_to_window(window_after)
    temp['driver'].maximize_window()
    current_url = temp['driver'].current_url
    assert(current_url=='https://justup.co/')

    return


e_init()
# v_LandingPage()
# e_btn_UploadClassify()
# v_LandingPage()
# e_btn_RealTimeBrowse()
# v_LandingPage()
# e_btn_Collaborate()
# v_LandingPage()
# e_btn_Top()
# v_LandingPage()
# e_btn_ShowDocPng()
# v_LandingPage()
# e_btn_ShowImagePng()
# v_LandingPage()
# e_btn_ShowMusicPng()
# v_LandingPage()
# e_btn_ShowVideoPng()
# v_LandingPage()


# e_footer_Twitter()
# v_TwitterPage()
# e_close_tab()

# v_LandingPage()

# e_footer_ServicePolicy()
# v_ServicePolicyPage()
# e_close_tab()

# v_LandingPage()

# e_footer_PrivacyPolicy()
# v_PrivacyPolicyPage()
# e_close_tab()

# v_LandingPage()

# e_footer_GooglePlus()
# v_GooglePlusPage()
# e_close_tab()

# v_LandingPage()

# e_footer_FB()
# v_FBPage()
# e_close_tab()

# v_LandingPage()

# e_footer_Blog()
# v_BlogPage()
# e_close_tab()



# e_btn_FreeRegister()
# v_RegisterPage()
# e_Register_icon_HomeLogo()

# v_LandingPage()

# e_btn_JustupSignup()
# v_RegisterPage()
# e_Register_icon_HomeLogo()

# v_LandingPage()

# e_btn_GetFreeSpace()
# v_RegisterPage()
# e_Register_icon_HomeLogo()

# v_LandingPage()


# e_btn_Login()
# v_LoginPage()
# e_Login_btn_ContactUs()
# v_LandingPage()