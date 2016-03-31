# -*- coding: utf-8 -*- 
import sys,os,re,stat
from string import Template

ttt=False
skip_value = True
old_contents=None
del_area=None
fun_list = []
script_fun_list = []
del_func_list = []

merged_str=''
del_area_start = '\'\'\'\n==================[Deleted functions, please check this]==================\n'
del_area_end = '\n=============================[Deleted functions]==========================\n\'\'\''


#read graphml function

current_locate=sys.argv[1]

sys.path.append(current_locate)


if os.path.exists(current_locate+'/script.py'):

	#Get all function(script.py)
	from script import * 

	for i in dir():	
	    if re.match('^e_|^v_|^V_',i):

	        fun_list.append(i)


	#Get del area
	with open(current_locate+'/script.py', 'r') as f:

		old_contents = f.read()

	if del_area_start in old_contents:
		find_area = re.findall(r'\n==================\[Deleted functions, please check this]==================\n([\s\S]*)\n=============================\[Deleted functions]==========================\n', old_contents)
		del_area = del_area_start+find_area[0]
		


if os.path.exists(current_locate+'/merged.py'):

	#Get all function(merged.py)
	with open(current_locate+'/merged.py', 'r') as f:

		merged_contents = f.read()
		

	find_area = re.findall(r'def ([\s\S]*)\n    return', merged_contents)

	merged_content_list = find_area[0].split('def ')

merged_func_list = []

for i in merged_content_list:
	merged_func_list.append(i[:i.find('() :')]) 

intersection = list(set(fun_list) & set(merged_func_list))
# print intersection.index('e_btn_Home_FROM_Drink_Page')
del_function = list(set(fun_list) ^ set(intersection))
# print del_function.index('e_btn_Home_FROM_Drink_Page')
new_function = list(set(merged_func_list) ^ set(intersection))
# print new_function.index('e_btn_Home_FROM_Drink_Page')

if os.path.exists(current_locate+'/script.py'):

	#Get all function(script.py)
	with open(current_locate+'/script.py', 'r') as f:

		script_contents = f.read()
		if del_area_start in script_contents:
			script_contents = script_contents[:script_contents.index(del_area_start)]

	find_area = re.findall(r'\ndef ([\s\S]*)\n    return', script_contents)

	script_content_list = find_area[0].split('\ndef ')

	script_content_list[-1]=script_content_list[-1]+'\n    return "'+script_content_list[-1][:script_content_list[-1].index('()')]+'"'

	for i in script_content_list:

		if del_area_start in i :
			script_content_temp= i[:i.index(del_area_start)]
			# print script_content_temp
		else:
			script_content_temp = i

		script_content_list[script_content_list.index(i)] = '\ndef '+script_content_temp

#del not exist func
deleted_function_list = []
script_content_list_final =[]


if del_function:

	for script_content_item in script_content_list:
		for del_item in del_function:
			pattern_temp = str(script_content_item[script_content_item.index('def ')+4:script_content_item.index('()')])
			if str(del_item) == pattern_temp:
				# print 'del_item:\n',del_item
				# print 'script_content_item:\n',script_content_item
				deleted_function_list.append(script_content_item)

# print deleted_function_list
#目前現存的script function
if old_contents:

	script_content_list_final = list(set(script_content_list) ^ set(deleted_function_list))


# print script_content_list_final
#input old data
if old_contents:
	pre_script_content =re.split('def ', old_contents)[0]

else:
	pre_script_content ="# -*- coding: utf-8 -*-\n\n\nglobal temp\ntemp={}\n\n\n\n"


#Add pre_script_content
Final_script = pre_script_content


#Add 現存的script function
all_script_content_list = script_content_list_final


#Add New function
if new_function:
	for i in new_function:
		new_str = '\ndef '+str(i)+'() :\n    print "'+str(i)+'"\n    global temp\n\n    return "'+str(i)+'"\n\n\n'

		all_script_content_list.append(new_str)

all_script_content_list = sorted(all_script_content_list,key = str.lower)  

for i in all_script_content_list:
	Final_script+=i

#Add del function
#存在舊的刪除區與新刪除的function
if del_area and deleted_function_list:

	Final_script+='\n\n'+del_area

	# print deleted_function_list
	for i in deleted_function_list:
		Final_script+=i	

	Final_script+=del_area_end

#只存在新刪除的function
elif deleted_function_list:
	Final_script+='\n\n'+del_area_start
	for i in deleted_function_list:
		Final_script+=i	
	Final_script+=del_area_end

#只存在舊的刪除區
elif del_area:
	Final_script+='\n\n'+del_area
	Final_script+=del_area_end



#Write to script.py
with open(current_locate+'/script.py', 'w') as f:
	f.write(str(Final_script))

os.chmod(current_locate+'/script.py', stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)	

#open merged.py
write_file = open(sys.argv[1]+'/merged.py','r')
merged_str = write_file.read()
merged_str = merged_str.replace(merged_str[merged_str.find('temp={}')+9:merged_str.find('#init parameter')],'\n\n\n\n\n\n\n\n') 

#write Runner.py 
write_file = open('/usr/local/GraphwalkerRunner/lib/Runner.py','w')

write_file.write(merged_str)
write_file.close()
