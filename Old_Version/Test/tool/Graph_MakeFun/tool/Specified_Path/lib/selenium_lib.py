# -*- coding: utf-8 -*-
import requests,json,traceback,time,sys,random
import xml.etree.cElementTree as ET

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


def SendKeys(driver,e_id,text):

	driver.find_element_by_id(e_id).clear()
	driver.find_element_by_id(e_id).send_keys(text)

def Click_By_id(driver,c_id):

	wait = WebDriverWait(driver, 10)
	wait.until(EC.visibility_of_element_located((By.ID,c_id)))
	wait.until(EC.element_to_be_clickable((By.ID,c_id)))

	driver.find_element_by_id(c_id).click()


def Get_Content_Length(driver,class_name):

	#get list len
	content_list = driver.find_elements_by_class_name(class_name)
	content_list_length = len(content_list)

	return content_list_length

def ScrollToBotton(driver,class_name):

	#get list len
	time.sleep(1)
	content_list_length_before = Get_Content_Length(driver,class_name)


	if content_list_length_before > 0:

		action = webdriver.ActionChains(driver)
		action.move_to_element(driver.find_element_by_id('select0')).click()
		action.move_to_element(driver.find_element_by_id('select0')).click()
		time.sleep(1)

		for i in range(1):
			action.send_keys(Keys.END).perform()
		time.sleep(1)

		content_list_length_after = Get_Content_Length(driver,class_name)

		#scrollTobotton
	
		while content_list_length_before != content_list_length_after:

			content_list_length_before = Get_Content_Length(driver,class_name)

			for i in range(1):
				
				action.send_keys(Keys.END).perform()
	    		
	    		time.sleep(1)
		    	content_list_length_after = Get_Content_Length(driver,class_name)	

def GetRandomItem(driver,class_name):

   	content_list = driver.find_elements_by_class_name(class_name)

	get_random = random.randint(0,len(content_list)-1)

	return get_random
	   	
def MoveToElement_By_id(driver,e_id,click=''):

	mte = driver.find_element_by_id(e_id)

	action = webdriver.ActionChains(driver)
	action.move_to_element(mte)
	time.sleep(1)
	if click=='left':
		action.click(mte)
	
	elif click == 'right':

		action.context_click(mte)

	action.perform()

def GetFileList(driver):
	
	#get all file list & pick one 
 	ScrollToBotton(driver,'for-row')

	#To Check file exist
	list_content_style = driver.find_element_by_id('list-content').get_attribute('style')
	if list_content_style =='display: none;':
				
		return None
	else:
	#
		content_list = driver.find_elements_by_class_name('for-row')
		file_list = {'All':[]}
		for i in content_list:
			if not file_list.has_key(i.get_attribute('data-type')):
				file_list[i.get_attribute('data-type')]=[]
			file_list[i.get_attribute('data-type')].append(i)
			file_list['All'].append(i)

		return file_list

def DragAndDrop(driver, source, target):

	action = webdriver.ActionChains(driver)
	action.drag_and_drop(source, target)
	action.move_to_element(target)
	action.perform()


	

def CheckFavorite(driver, fav_obj_style, get_file_id):
	fileid = [] 
	wait = WebDriverWait(driver, 10)

	#if file has joined Favorites
	if fav_obj_style == 'color: rgb(255, 194, 51);':

		#go fav page & check file not exist

		Click_By_id(driver,"quick-go-favrite")

		time.sleep(2)

		file_list = GetFileList(driver)

		if file_list != None:

			All_list = file_list['All']

			for i in All_list:
				assert i.get_attribute('data-fileid') != str(get_file_id),'List contains file'

	#if file has not joined Favorites
	elif fav_obj_style == '':

		#go fav page & check file exist

		Click_By_id(driver,"quick-go-favrite")

		time.sleep(2)

		file_list = GetFileList(driver)

		All_list = file_list['All']
		
		for i in All_list:
			fileid.append(i.get_attribute("data-fileid"))

		assert get_file_id in fileid , 'List does not contains file'

	#exception occured
	else:
		print 'exception occured'

	#back to all file 
	Click_By_id(driver,"quick-go-all-file")


def Rename(driver, select_name):

	name = select_name.split('_')

	if len(name) > 1 and name[-1] == 'rename':
		
		SendKeys(driver,"input-file-name",str(name[0])+"_rename_1")

	elif len(name) > 2 and name[-2] == 'rename':
			
		count_index = str(int(name[-1])+1)

		SendKeys(driver,"input-file-name",str(name[0])+"_rename_"+str(count_index))
	
	else:
				
		SendKeys(driver,"input-file-name",str(name[0])+"_rename")

	driver.find_element_by_id("manipulate-left-btn").click()


def GetTagList(driver):

	tag_list = {'tag_name':[]}

	content_list = driver.find_elements_by_xpath("//div[@id='tags-rowTHIS']/*")

	for i in content_list:

		if 'edit-tag-name-style' in str(i.get_attribute('class')):
			tag_name = driver.find_element_by_id(i.get_attribute('id')).text
			tag_list['tag_name'].append(str(tag_name[:-1]))

	return tag_list['tag_name']

def AddTag(driver):

	tag_list = GetTagList(driver)

	tag_loop = True
	tag_index = 0
	tag_name = 'Tag_'+ str(tag_index)
	
	while(tag_loop):
		if tag_name in tag_list:
			tag_index+=1
			tag_name = 'Tag_'+ str(tag_index)
		else:
			tag_loop = False

	SendKeys(driver,'input-tag-name',tag_name)
	
	driver.find_element_by_class_name('dialog-footer').click()
	time.sleep(1)

	
def WaitAlertContent(driver,e_id):
	alertContent = driver.find_element_by_id(e_id).text

	count = 0
	while(not alertContent and count < 6):
		count += 1
		alertContent = driver.find_element_by_id(e_id).text
		time.sleep(0.5)

	return alertContent

def WaitElement(driver,c_id):

	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.visibility_of_element_located((By.ID,c_id)))

	return element