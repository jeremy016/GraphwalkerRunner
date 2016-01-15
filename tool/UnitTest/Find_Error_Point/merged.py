
import requests,json,time
##
## 1) Generate python stub source code:
##    java -jar graphwalker-3.4.0-SNAPSHOT.jar source -i model.graphml python.template > model.py
##
## 2) Start graphwalker:
##    java -jar graphwalker-3.4.0-SNAPSHOT.jar online --json --service RESTFUL -m model.graphml "random(edge_coverage(100))"
##
## 3) Run the per program:
##    python model.py
##



def e_ContactUs_btn_Cancel() :
    return "e_ContactUs_btn_Cancel"




def e_ContactUs_btn_Submit_NullEmail() :
    return "e_ContactUs_btn_Submit_NullEmail"




def e_ContactUs_btn_Submit_NullName() :
    return "e_ContactUs_btn_Submit_NullName"




def e_ContactUs_btn_Submit_NullOpinions() :
    return "e_ContactUs_btn_Submit_NullOpinions"




def e_ContactUs_btn_Submit_Pass() :
    return "e_ContactUs_btn_Submit_Pass"




def e_ForgetPassword_btn_Submit_EmailNotUse() :
    return "e_ForgetPassword_btn_Submit_EmailNotUse"




def e_ForgetPassword_btn_Submit_ForgetPassword_Pass() :
    return "e_ForgetPassword_btn_Submit_ForgetPassword_Pass"




def e_ForgetPassword_btn_Submit_FormatError() :
    return "e_ForgetPassword_btn_Submit_FormatError"




def e_ForgetPassword_btn_Submit_NullEmail() :
    return "e_ForgetPassword_btn_Submit_NullEmail"




def e_ForgetPassword_btn_backLoginPage() :
    return "e_ForgetPassword_btn_backLoginPage"




def e_ForgetPassword_icon_BackLogin() :
    return "e_ForgetPassword_icon_BackLogin"




def e_LoginFooter_ContactUs() :
    return "e_LoginFooter_ContactUs"




def e_Login_Footer_Blog() :
    return "e_Login_Footer_Blog"




def e_Login_Footer_ServicePolicy() :
    return "e_Login_Footer_ServicePolicy"




def e_Login_btn_ContactUs() :
    return "e_Login_btn_ContactUs"




def e_Login_btn_ForgotPassword() :
    return "e_Login_btn_ForgotPassword"




def e_Login_icon_Reload() :
    return "e_Login_icon_Reload"




def e_Main_Logout() :
    return "e_Main_Logout"




def e_Register_icon_HomeLogo() :
    return "e_Register_icon_HomeLogo"




def e_Register_icon_LoginLogo() :
    return "e_Register_icon_LoginLogo"




def e_btn_CloseContactWindows() :
    return "e_btn_CloseContactWindows"




def e_btn_Collaborate() :
    return "e_btn_Collaborate"




def e_btn_FreeRegister() :
    return "e_btn_FreeRegister"




def e_btn_GetFreeSpace() :
    return "e_btn_GetFreeSpace"




def e_btn_JustupSignup() :
    return "e_btn_JustupSignup"




def e_btn_Login() :
    return "e_btn_Login"




def e_btn_LoginPass() :
    return "e_btn_LoginPass"




def e_btn_LoginRegister() :
    return "e_btn_LoginRegister"




def e_btn_Login_LoginFail() :
    return "e_btn_Login_LoginFail"




def e_btn_Login_NoAccountPassword() :
    return "e_btn_Login_NoAccountPassword"




def e_btn_Login_NoPassword() :
    return "e_btn_Login_NoPassword"




def e_btn_RealTimeBrowse() :
    return "e_btn_RealTimeBrowse"




def e_btn_ShowDocPng() :
    return "e_btn_ShowDocPng"




def e_btn_ShowImagePng() :
    return "e_btn_ShowImagePng"




def e_btn_ShowMusicPng() :
    return "e_btn_ShowMusicPng"




def e_btn_ShowVideoPng() :
    return "e_btn_ShowVideoPng"




def e_btn_Top() :
    return "e_btn_Top"




def e_btn_UploadClassify() :
    return "e_btn_UploadClassify"




def e_close_tab() :
    return "e_close_tab"




def e_footer_Blog() :
    return "e_footer_Blog"




def e_footer_FB() :
    return "e_footer_FB"




def e_footer_GooglePlus() :
    return "e_footer_GooglePlus"




def e_footer_PrivacyPolicy() :
    return "e_footer_PrivacyPolicy"




def e_footer_ServicePolicy() :
    return "e_footer_ServicePolicy"




def e_footer_Twitter() :
    return "e_footer_Twitter"




def e_init() :
    return "e_init"




def v_ChangePasswordMessagePage() :
    return "v_ChangePasswordMessagePage"




def v_ForgetPasswordPage() :
    return "v_ForgetPasswordPage"




def v_JustupMainPage() :
    return "v_JustupMainPage"




def v_LandingPage() :
    return "v_LandingPage"




def v_Landing_BlogPage() :
    return "v_Landing_BlogPage"




def v_Landing_FBPage() :
    return "v_Landing_FBPage"




def v_Landing_GooglePlusPage() :
    return "v_Landing_GooglePlusPage"




def v_Landing_PrivacyPolicyPage() :
    return "v_Landing_PrivacyPolicyPage"




def v_Landing_ServicePolicyPage() :
    return "v_Landing_ServicePolicyPage"




def v_Landing_TwitterPage() :
    return "v_Landing_TwitterPage"




def v_LoginPage() :
    return "v_LoginPage"




def v_Login_BlogPage() :
    return "v_Login_BlogPage"




def v_Login_PrivacyPolicyPage() :
    return "v_Login_PrivacyPolicyPage"




def v_Login_ServicePolicyPage() :
    return "v_Login_ServicePolicyPage"




def v_Login_footer_ContactUs() :
    return "v_Login_footer_ContactUs"




def v_RegisterPage() :
    return "v_RegisterPage"




fun_list=[]

with open('fun_name.txt', 'r') as file:

    for line in file:
        fun_list.append(line.strip('\n'))


fun_list_len = len(fun_list)
print 'list length : '+str(fun_list_len)

gw_url = 'http://localhost:8887/graphwalker'
t0 = time.time()
while requests.get(gw_url+'/hasNext').json()['HasNext'] == 'true' :
    
    step = requests.get(gw_url+'/getNext').json()['CurrentElementName']

    if step != '' :

        result = eval( step + "()" )

        len_before = len(fun_list)

        if result in fun_list:
        
        	fun_list.remove(result)
        
        len_after = len(fun_list)

        if len_before == len_after:
            count+=1
        else:
            count=0
        if count == fun_list_len * fun_list_len:
            print "\n=============================="
            print 'count = length * length '
            print "=============================="
            break

t1 = time.time()
total = t1-t0
print '\nSpend time:'+str(total)
print '\nerror point : '
print fun_list

