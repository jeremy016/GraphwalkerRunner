# -*- coding: utf-8 -*-
import requests,json,traceback,time,sys,os
import xml.etree.cElementTree as ET

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import lib.selenium_lib as SL
import lib.GraphFun as GraphFun

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

def e_Login_btn_ContactUs():
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

def e_btn_Login_NoAccountPassword():
    global temp

    print( "e_btn_Login_NoAccountPassword" )

    temp['driver'].find_element_by_id("uemail").clear()
    temp['driver'].find_element_by_id("uemail").send_keys("")
    temp['driver'].find_element_by_id("upasswd").clear()
    temp['driver'].find_element_by_id("upasswd").send_keys("")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'login-button')))

    temp['driver'].find_element_by_id("login-button").click()

    alertContent = SL.WaitAlertContent(temp['driver'],"alertContent")
    temp['driver'].find_elements_by_xpath("//div[@id='alertMessage']/button")[0].click()

    assert(alertContent==temp['Language']['enter_user_email'])

    return



def e_btn_Login_NoPassword():
    global temp

    print( "e_btn_Login_NoPassword" )
    
    temp['driver'].find_element_by_id("uemail").clear()
    temp['driver'].find_element_by_id("uemail").send_keys("lumy")
    temp['driver'].find_element_by_id("upasswd").clear()
    temp['driver'].find_element_by_id("upasswd").send_keys("")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'login-button')))
    SL.Click_By_id(temp['driver'],"login-button")

    alertContent = SL.WaitAlertContent(temp['driver'],"alertContent")
    temp['driver'].find_elements_by_xpath("//div[@id='alertMessage']/button")[0].click()

    assert(alertContent==temp['Language']['entet_password'])

    return

def e_btn_Login_LoginFail():
    global temp

    print( "e_btn_Login_LoginFail" )
    
    temp['driver'].find_element_by_id("uemail").clear()
    temp['driver'].find_element_by_id("uemail").send_keys("lumy")
    temp['driver'].find_element_by_id("upasswd").clear()
    temp['driver'].find_element_by_id("upasswd").send_keys("123")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'login-button')))
    temp['driver'].find_element_by_id("login-button").click()

    alertContent = SL.WaitAlertContent(temp['driver'],"alertContent")
    
    temp['driver'].find_elements_by_xpath("//div[@id='alertMessage']/button")[0].click()

    assert(alertContent==temp['Language']['login_fail'])
    
    return  

def e_Login_icon_Reload():
    global temp

    print( "e_Login_icon_Reload" )

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'login-logo')))
    temp['driver'].find_element_by_id("login-logo").click()

    return

def e_Login_btn_ForgotPassword():
    global temp
    print( "e_Login_btn_ForgotPassword" )

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'login-forget')))
    temp['driver'].find_element_by_id("login-forget").click()

    return
    
def v_ForgetPasswordPage():
    global temp

    print( "v_ForgetPasswordPage" )
    if len(temp['driver'].window_handles) > 1:

        window_before = temp['driver'].window_handles[-2]
        window_after = temp['driver'].window_handles[-1]

        temp['driver'].close()
        temp['driver'].switch_to_window(window_after)
        temp['driver'].maximize_window()

    current_url = temp['driver'].current_url

    assert(current_url=='https://justup.co/account/forgot?continue=https%3A%2F%2Fjustup.co%2Faccount%2Foauth%2Fauthorize%3Fclient_id%3D7iIh8fEEJYryonH7TPFL%26redirect_uri%3Dhttps%253A%252F%252Fjustup.co%252Fapi%252Fv1.1%252Fauth%253Fmethod%253Ddoauth2%26response_type%3Dcode%26scope%3Dprofile')
    time.sleep(2)
    return

def e_ForgetPassword_icon_BackLogin():
    global temp
    print( "e_ForgetPassword_icon_BackLogin" )

    temp['driver'].find_elements_by_class_name('home-logo')[0].click()

    return

def e_ForgetPassword_btn_Submit_NullEmail():
    global temp

    print( "e_ForgetPassword_btn_Submit_NullEmail" )

    temp['driver'].find_element_by_id("userEmail").clear()
    temp['driver'].find_element_by_id("userEmail").send_keys("")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'btnSubmit')))
    temp['driver'].find_element_by_id("btnSubmit").click()

    alertContent = SL.WaitAlertContent(temp['driver'],"alertContent")

    assert(alertContent==temp['Language']['enter_mail_reset_password'])

    temp['driver'].find_elements_by_xpath("//div[@id='alertMessage']/button")[0].click()

    time.sleep(1)

    return

def e_ForgetPassword_btn_Submit_FormatError():
    global temp

    print( "e_ForgetPassword_btn_Submit_FormatError" )

    temp['driver'].find_element_by_id("userEmail").clear()
    temp['driver'].find_element_by_id("userEmail").send_keys("ssss")
    
    temp['wait'].until(EC.element_to_be_clickable((By.ID,'btnSubmit')))
    temp['driver'].find_element_by_id("btnSubmit").click()

    alertContent = SL.WaitAlertContent(temp['driver'],"alertContent")
    
    assert(alertContent==temp['Language']['email_format_error'])

    temp['driver'].find_elements_by_xpath("//div[@id='alertMessage']/button")[0].click()

    time.sleep(1)

    return

def e_ForgetPassword_btn_Submit_EmailNotUse():

    global temp

    print( "e_ForgetPassword_btn_Submit_EmailNotUse" )

    temp['driver'].find_element_by_id("userEmail").clear()
    temp['driver'].find_element_by_id("userEmail").send_keys("ssss@gmail.com")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'btnSubmit')))
    temp['driver'].find_element_by_id("btnSubmit").click()

    alertContent = SL.WaitAlertContent(temp['driver'],"alertContent")

    assert(alertContent==temp['Language']['email_not_found'])

    temp['driver'].find_elements_by_xpath("//div[@id='alertMessage']/button")[0].click()

    time.sleep(1)

    return

def e_ForgetPassword_btn_Submit_ForgetPassword_Pass():
    global temp

    print( "e_ForgetPassword_btn_Submit_ForgetPassword_Pass" )

    temp['driver'].find_element_by_id("userEmail").clear()
    temp['driver'].find_element_by_id("userEmail").send_keys('hh.idbg.test@gmail.com')
        
    temp['wait'].until(EC.element_to_be_clickable((By.ID,'btnSubmit')))
    temp['driver'].find_element_by_id("btnSubmit").click()

    buttonContent = SL.WaitAlertContent(temp['driver'],"btnSubmit")
 
    assert(buttonContent==temp['Language']['sending_wait'])

    return

def v_ChangePasswordMessagePage():
    global temp

    print( "v_ChangePasswordMessagePage" )
    
    temp['wait'].until(EC.element_to_be_clickable((By.ID,'forgetpwd-ok-msg')))    

    msgContent = SL.WaitAlertContent(temp['driver'],"forgetpwd-ok-msg")

    assert(msgContent==temp['Language']['feedback_message'])

    return

def e_ForgetPassword_btn_backLoginPage():

    global temp

    print( "e_ForgetPassword_btn_backLoginPage" )

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'forgetpwd-continue-link')))
    temp['driver'].find_element_by_id("forgetpwd-continue-link").click()

    return

def e_btn_LoginRegister():
    global temp
    print( "e_btn_LoginRegister")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'login-register')))
    temp['driver'].find_element_by_id("login-register").click()

    return


def v_RegisterPage() :
    global temp
    print( "v_RegisterPage" )
    
    RegisterPage = temp['driver'].find_element_by_id('userRegister')
    assert(type(RegisterPage).__name__=='WebElement')
    return

def e_Register_icon_LoginLogo() :
    global temp
    print( "e_Register_icon_LoginLogo" )
    temp['driver'].find_elements_by_class_name('login-logo')[0].click()
    return

def e_LoginFooter_ContactUs():
    global temp
    print( "e_LoginFooter_ContactUs" )
    
    temp['driver'].find_element_by_xpath("//table[@id='login-right-link']/tbody/tr/td[5]").click()

    return

def v_Login_footer_ContactUs():
    global temp
    print( "v_Login_footer_ContactUs" )

    temp['driver'].find_elements_by_class_name('modal-content')

    return
    
def e_ContactUs_btn_Submit_NullName():
    global temp
    print( "e_ContactUs_btn_Submit_NullName" )

    SL.WaitElement(temp['driver'],'name')

    temp['driver'].find_element_by_id("name").clear()
    temp['driver'].find_element_by_id("name").send_keys("")

    temp['driver'].find_element_by_id("email").clear()
    temp['driver'].find_element_by_id("email").send_keys("")

    temp['driver'].find_element_by_id("comment").clear()
    temp['driver'].find_element_by_id("comment").send_keys("")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'btnSubmit')))
    temp['driver'].find_element_by_id("btnSubmit").click()

    nameStatus = SL.WaitAlertContent(temp['driver'],"nameStatus")
    
    assert(nameStatus==temp['Language']['enter_name'])
    return

def e_ContactUs_btn_Submit_NullEmail():
    global temp
    print( "e_ContactUs_btn_Submit_NullEmail" )

    SL.WaitElement(temp['driver'],'name')

    temp['driver'].find_element_by_id("name").clear()
    temp['driver'].find_element_by_id("name").send_keys("Tester")

    temp['driver'].find_element_by_id("email").clear()
    temp['driver'].find_element_by_id("email").send_keys("")

    temp['driver'].find_element_by_id("comment").clear()
    temp['driver'].find_element_by_id("comment").send_keys("")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'btnSubmit')))
    temp['driver'].find_element_by_id("btnSubmit").click()

    emailStatus = SL.WaitAlertContent(temp['driver'],"emailStatus")

    assert(emailStatus==temp['Language']['enter_mail'])
    return

def e_ContactUs_btn_Submit_NullOpinions():
    global temp
    print( "e_ContactUs_btn_Submit_NullOpinions" )

    SL.WaitElement(temp['driver'],'name')

    temp['driver'].find_element_by_id("name").clear()
    temp['driver'].find_element_by_id("name").send_keys("Tester")

    temp['driver'].find_element_by_id("email").clear()
    temp['driver'].find_element_by_id("email").send_keys("hh.idbg.test@gmail.com")

    temp['driver'].find_element_by_id("comment").clear()
    temp['driver'].find_element_by_id("comment").send_keys("")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'btnSubmit')))
    temp['driver'].find_element_by_id("btnSubmit").click()
    
    commentStatus = SL.WaitAlertContent(temp['driver'],"commentStatus")
    
    assert(commentStatus==temp['Language']['enter_comments'])
    return


def e_btn_CloseContactWindows() :
    global temp
    print( "e_btn_CloseContactWindows" )

    SL.WaitElement(temp['driver'],'contactForm')
    temp['driver'].find_elements_by_xpath("//form[@id='contactForm']/div/div/div/button")[0].click()
    time.sleep(1)

    return

def e_ContactUs_btn_Submit_Pass():
    global temp
    print( "e_ContactUs_btn_Submit_Pass" )

    SL.WaitElement(temp['driver'],'name')

    temp['driver'].find_element_by_id("name").clear()
    temp['driver'].find_element_by_id("name").send_keys("Tester")

    temp['driver'].find_element_by_id("email").clear()
    temp['driver'].find_element_by_id("email").send_keys("hh.idbg.test@gmail.com")

    temp['driver'].find_element_by_id("comment").clear()
    temp['driver'].find_element_by_id("comment").send_keys("Testing...")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'btnSubmit')))

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'btnSubmit')))
    temp['driver'].find_element_by_id("btnSubmit").click()

    #alertContent - LoginPage

    alertContent = SL.WaitAlertContent(temp['driver'],"alertContent")
    temp['driver'].find_elements_by_xpath("//div[@id='alertMessage']/button")[0].click()

    assert(alertContent==temp['Language']['success_reply_soon'])
    return

def e_ContactUs_btn_Cancel():
    global temp
    print( "e_ContactUs_btn_Cancel" )
    
    temp['wait'].until(EC.element_to_be_clickable((By.ID,'btn-return')))
    temp['driver'].find_element_by_id("btn-return").click()
    return
    
def e_Login_Footer_ServicePolicy():
    global temp
    print( "e_Login_Footer_ServicePolicy" )
    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight);")
    temp['driver'].find_elements_by_xpath("//table[@id='login-right-link']/tbody/tr/td[3]/a")[0].click()

    return


def v_Login_ServicePolicyPage() :
    global temp
    print( "v_Login_ServicePolicyPage" )

    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]
    temp['driver'].switch_to_window(window_after)

    current_url = temp['driver'].current_url
    assert(current_url=='http://web.9ifriend.com/drive/policy.html')

    return

def e_Login_Footer_Blog():
    global temp
    print( "e_Login_Footer_Blog" )

    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
    temp['driver'].find_elements_by_xpath("//table[@id='login-right-link']/tbody/tr/td[2]/a")[0].click()

    return


def v_Login_BlogPage() :
    global temp
    print( "v_Login_BlogPage" )
    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]
    temp['driver'].switch_to_window(window_after)

    current_url = temp['driver'].current_url
    assert(current_url=='https://blog.justup.co/')
    return



def e_Login_Footer_PrivacyPolicy():
    global temp
    print( "e_Login_Footer_PrivacyPolicy" )

    temp['driver'].execute_script("window.scrollTo(0, document.body.scrollHeight);")

    temp['driver'].find_elements_by_xpath("//table[@id='login-right-link']/tbody/tr/td[4]/a")[0].click()

    return


def v_Login_PrivacyPolicyPage():
    global temp
    print( "v_Login_PrivacyPolicyPage" )
    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]
    temp['driver'].switch_to_window(window_after)

    current_url = temp['driver'].current_url
    assert(current_url=='http://web.9ifriend.com/policies/index.html')
    return
    

def e_Login_close_tab() :
    global temp
    print( "e_Login_close_tab" )
    window_before = temp['driver'].window_handles[-2]
    window_after = temp['driver'].window_handles[-1]

    temp['driver'].close()
    temp['driver'].switch_to_window(window_before)
    current_url = temp['driver'].current_url

    return

def e_btn_LoginPass():
    global temp
    print( "e_btn_LoginPass" )

    temp['driver'].find_element_by_id("uemail").clear()
    temp['driver'].find_element_by_id("uemail").send_keys("hh.idbg.test@gmail.com")
    temp['driver'].find_element_by_id("upasswd").clear()
    temp['driver'].find_element_by_id("upasswd").send_keys("hh888888")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'login-button')))
    temp['driver'].find_element_by_id("login-button").click()

    return

def v_JustupMainPage():
    global temp
    print( "v_JustupMainPage" )
    
    element = SL.WaitElement(temp['driver'],"main-logo")
    
    assert(type(element).__name__=='WebElement')

    return

def e_Main_Logout():
    global temp
    print( "e_Main_Logout" )

    SL.WaitElement(temp['driver'],"avatar-img")
    SL.WaitElement(temp['driver'],"quick-icon-area")

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'user-avatar')))

    SL.MoveToElement_By_id(temp['driver'],"user-avatar",click='left')

    temp['wait'].until(EC.element_to_be_clickable((By.ID,'log-out')))

    temp['driver'].find_element_by_id("log-out").click()

    return



