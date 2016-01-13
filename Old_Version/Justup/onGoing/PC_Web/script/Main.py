# -*- coding: utf-8 -*-
import requests,json,traceback,time,sys,random
import xml.etree.cElementTree as ET

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import lib.selenium_lib as SL

global temp
temp={}

temp['driver'] = webdriver.Firefox()
temp['action'] = webdriver.ActionChains(temp['driver'])
temp['wait'] = WebDriverWait(temp['driver'], 10)
temp['driver'].maximize_window()

temp['driver'].get('https://justup.9ifriend.com/')
temp['driver'].find_element_by_id('just-login').click()


def v_LoginPage() :
    global temp
    print( "v_LoginPage" )


    element = temp['wait'].until(EC.visibility_of_element_located((By.ID,'userLogin')))

    RegisterPage = temp['driver'].find_element_by_id('userLogin')

    assert(type(RegisterPage).__name__=='WebElement')

    return

def e_btn_LoginPass():
	global temp
	print( "e_btn_LoginPass" )

	SL.SendKeys(temp['driver'],"uemail","Tester002")
	SL.SendKeys(temp['driver'],"upasswd","Aa123456")
	
	SL.Click_By_id(temp['driver'],"login-button")

	return

def v_JustupMainPage():
	global temp
	print( "v_JustupMainPage" )

	element = temp['wait'].until(EC.visibility_of_element_located((By.ID,'crumb-parent')))
	
	return

def e_Main_Logout():
	global temp
	print( "e_Main_Logout" )

	element = temp['wait'].until(EC.visibility_of_element_located((By.ID,'user-avatar')))
	time.sleep(2)

	SL.Click_By_id(temp['driver'],"user-avatar")

	SL.Click_By_id(temp['driver'],"log-out")

	return

def e_Main_CreateNewFolder():
	global temp
	print( "e_Main_CreateNewFolder" )

	SL.ScrollToBotton(temp['driver'],'for-row')
	
	content_list_length = SL.Get_Content_Length(temp['driver'],'for-row')

	time.sleep(1)
	SL.Click_By_id(temp['driver'],"new-folder-button")

	element = temp['wait'].until(EC.visibility_of_element_located((By.ID,'create-folder-dialog')))

	SL.SendKeys(temp['driver'],"new-folder-name","Creat Folder Testing")

	SL.Click_By_id(temp['driver'],"create-folder-save-btn")

	SL.ScrollToBotton(temp['driver'],'for-row')
	content_list_after_length = SL.Get_Content_Length(temp['driver'],'for-row')
	time.sleep(2)
	assert(content_list_length+1 == content_list_after_length)

def e_Main_MoveToElement_Delete():
	global temp
	print( "e_Main_MoveToElement_Delete" )

	folder_list_length = len(temp['file_list']['All'])

	#get index
	get_num = temp['random_one'].get_attribute('id')[3:]
	
	btn_delete = "btn-delete"+str(get_num)
	
	SL.Click_By_id(temp['driver'],btn_delete)

	file_list = SL.GetFileList(temp['driver'])

	folder_list_after_length = len(file_list['All'])

	assert(folder_list_after_length == folder_list_length-1)

def e_Main_Checkbox_Delete(): 
	global temp
	print( "e_Main_Checkbox_Delete" )

	folder_list_length = len(temp['file_list']['All'])

	time.sleep(2)

	SL.Click_By_id(temp['driver'],"btn-delete")

	SL.ScrollToBotton(temp['driver'],'for-row')

	file_list = SL.GetFileList(temp['driver'])

	folder_list_after_length = len(file_list['All'])

	assert(folder_list_after_length == folder_list_length-1)


def e_Main_RightClick_Delete():  
	global temp
	print( "e_Main_RightClick_Delete" )

	folder_list_length = len(temp['file_list']['All'])

	SL.Click_By_id(temp['driver'],"right-click-item-delete")

	SL.ScrollToBotton(temp['driver'],'for-row')

	file_list = SL.GetFileList(temp['driver'])

	folder_list_after_length = len(file_list['All'])

	assert(folder_list_after_length == folder_list_length-1)

def e_Main_ChangeListModule():
	global temp
	print( "e_Main_ChangeListModule")

	module_List = ['fileList','pictureList']

	before_List = temp['driver'].find_element_by_id("data-area").get_attribute('class')
	
	module_List.remove(before_List)

	SL.Click_By_id(temp['driver'],"switch-display-mode-icon")
	time.sleep(1)
	after_List = temp['driver'].find_element_by_id("data-area").get_attribute('class')
	
	assert(after_List == module_List[0])
	# class fileList pictureList

def e_Main_MoveToElement_Favorite():
	global temp
	print( "e_Main_MoveToElement_Favorite")

	#get index
	get_num = temp['random_one'].get_attribute('id')[3:]
	
	btn_fav = "btn-fav"+str(get_num)

	fav_obj_style = temp['driver'].find_element_by_id(btn_fav).get_attribute("style")

	get_file_id = temp['random_one'].get_attribute("data-fileid")

	SL.Click_By_id(temp['driver'],btn_fav)

	SL.CheckFavorite(temp['driver'], fav_obj_style, get_file_id)


def e_Main_RightClick_Favorite():
	global temp
	print( "e_Main_RightClick_Favorite")

	#Click favorite
	SL.Click_By_id(temp['driver'],"right-click-item-myfavorite")
	
	#Check right or not
	get_num = temp['random_one'].get_attribute('id')[3:]

	btn_fav = "btn-fav"+str(get_num)

	fav_obj_style = temp['driver'].find_element_by_id(btn_fav).get_attribute("style")

	get_file_id = temp['random_one'].get_attribute("data-fileid")

	SL.CheckFavorite(temp['driver'], fav_obj_style, get_file_id)

	

def e_Main_CheckBox_Rename():
	global temp
	print( "e_Main_CheckBox_Rename")

	time.sleep(2)

	temp['driver'].find_element_by_id("btn-rename").click()


def e_Main_RightClick_Rename():
	global temp
	print( "e_Main_RightClick_Rename")

	#Click rename
	SL.Click_By_id(temp['driver'],"right-click-item-rename")


def v_Main_Rename():
	global temp
	print( "v_Main_Rename")

	temp['wait'].until(EC.visibility_of_element_located((By.ID,"input-file-name")))

def e_Main_InputNewName():
	global temp
	print( "v_Main_InputNewName")

	input_box = temp['driver'].find_element_by_xpath("//input[@id='input-file-name']/..")

	get_num = input_box.get_attribute('id')[10:]
		
	select_name = "finfo-name"+str(get_num)

	name = temp['driver'].find_element_by_id('input-file-name').get_attribute('name')
	
	SL.Rename(temp['driver'],name)

	SL.ScrollToBotton(temp['driver'],'for-row')

	assert name != temp['driver'].find_element_by_id(select_name).text ,'Rename Fail'


def e_Main_MoveToElement_AddTag():
	global temp
	print( "e_Main_MoveToElement_AddTag")

	#get index
	get_num = temp['random_one'].get_attribute('id')[3:]
	
	btn_fav = "tagicon"+str(get_num)

	SL.Click_By_id(temp['driver'],btn_fav)


	#clean temp data
	del temp['random_one']


def e_Main_RightClick_AddTag():
	global temp
	print( "e_Main_RightClick_AddTag")

	SL.Click_By_id(temp['driver'],"right-click-item-addtag")


def e_Main_CheckBox_AddTag():
	global temp
	print( "e_Main_CheckBox_AddTag")

	time.sleep(2)

	temp['driver'].find_element_by_id("btn-tag").click()
	

def v_Main_TagSetting():
	global temp
	print( "v_Main_TagSetting")

	temp['wait'].until(EC.visibility_of_element_located((By.ID,"tag-edit-dialog")))

def e_Main_CheckBox_RandomOne():
	global temp
	print( "e_Main_RightClick_RandomOne")

	file_list = SL.GetFileList(temp['driver'])
	
	random_one = random.choice(file_list['All'])

	#get index
	temp['file_list'] = file_list

	get_num = random_one.get_attribute('id')[3:]

	select_id = "select"+str(get_num)
	
	select_name = "finfo-name"+str(get_num)
	
	name = temp['driver'].find_element_by_id(select_name).text

	temp['driver'].find_element_by_id(select_id).click()


def v_Main_CheckBox():
	global temp
	print( "v_Main_CheckBox")

	temp['wait'].until(EC.visibility_of_element_located((By.ID,"selected-file-count")))


def e_Main_RightClick_RandomOne():
	global temp
	print( "e_Main_RightClick_RandomOne")

	file_list = SL.GetFileList(temp['driver'])
	
	random_one = random.choice(file_list['All'])

	#get index
	temp['random_one'] = random_one
	temp['file_list'] = file_list

	get_num = random_one.get_attribute('id')[3:]

	select_id = random_one.get_attribute('id')

	select_name = "finfo-name"+str(get_num)
	
	name = temp['driver'].find_element_by_id(select_name).text

	SL.MoveToElement_By_id(temp['driver'],select_id,'right')


def v_Main_RightClickMenu():
	global temp
	print( "v_Main_RightClickMenu")

	temp['wait'].until(EC.visibility_of_element_located((By.ID,"right-click-menu")))


def e_Main_MoveToElement_RandomOne():
	global temp
	print( "e_Main_MoveToElement_RandomOne")

	file_list = SL.GetFileList(temp['driver'])
	
	random_one = random.choice(file_list['All'])

	#get index
	temp['random_one'] = random_one
	temp['file_list'] = file_list
	
	SL.MoveToElement_By_id(temp['driver'],random_one.get_attribute('id'))

def v_Main_MoveToElement():
	global temp
	print( "v_Main_MoveToElement")

	time.sleep(2)

	get_index = temp['random_one'].get_attribute('id')[3:]
	
	temp['wait'].until(EC.visibility_of_element_located((By.ID,"btn-group"+str(get_index))))

def e_Main_AddNewTag():
	global temp
	print( "e_Main_AddNewTag")

	SL.AddTag(temp['driver'])

	Click_By_id(driver,'tag-save-btn')

def e_Main_AddDuplicateTag():
	global temp
	print( "e_Main_AddDuplicateTag")

	if not SL.GetTagList(temp['driver']):
	
		SL.AddTag(temp['driver'])

	SL.SendKeys(temp['driver'],'input-tag-name',SL.GetTagList(temp['driver'])[0])

	temp['driver'].find_element_by_class_name('dialog-footer').click()

	SL.Click_By_id(temp['driver'],'warning-btn-ok')

	SL.Click_By_id(temp['driver'],'tag-save-btn')

##################################################################################################################################

# v_LoginPage()

# e_btn_LoginPass()

# v_JustupMainPage()

### MoveToElement ###
# e_Main_MoveToElement_RandomOne()

# v_Main_MoveToElement()

# e_Main_MoveToElement_AddTag()

# e_Main_MoveToElement_Favorite()

# e_Main_MoveToElement_Delete()


### RightClick ###
# e_Main_RightClick_RandomOne()

# v_Main_RightClickMenu()

# e_Main_RightClick_AddTag()

# e_Main_RightClick_Rename()

# e_Main_RightClick_Favorite()

# e_Main_RightClick_Delete()


### CheckBox ###
# e_Main_CheckBox_RandomOne()

# v_Main_CheckBox()

# e_Main_CheckBox_Rename()

# e_Main_Checkbox_Delete()

# e_Main_CheckBox_AddTag()


### Tag ###
# v_Main_TagSetting()

# e_Main_AddNewTag()

# e_Main_AddDuplicateTag()

### relay - Rename ###
# v_Main_Rename()
# e_Main_InputNewName()


## Main ###
# e_Main_CreateNewFolder()

# e_Main_ChangeListModule()


