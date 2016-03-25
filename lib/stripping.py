# -*- coding: utf-8 -*- 
import sys,os,re
from string import Template

ttt=False
skip_value = True
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
		#print 'del area\n',del_area

	else:
		del_area = del_area_start


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

del_function = list(set(fun_list) ^ set(intersection))

new_function = list(set(merged_func_list) ^ set(intersection))



if os.path.exists(current_locate+'/script.py'):

	#Get all function(merged.py)
	with open(current_locate+'/script.py', 'r') as f:

		script_contents = f.read()

	find_area = re.findall(r'def ([\s\S]*)\n    return', script_contents)

	script_content_list = find_area[0].split('def ')

	script_content_list[-1]=script_content_list[-1]+'\n    return "'+script_content_list[-1][:script_content_list[-1].index('()')]+'"'

for i in script_content_list:
	script_content_list[script_content_list.index(i)] = '\ndef '+i

#del not exist func
deleted_function_list = []
script_content_list_final =[]


if del_function:

	for script_content_item in script_content_list:
		for del_item in del_function:
			if str(del_item) in str(script_content_item):
				# print 'del_item:\n',del_item
				# print 'script_content_item:\n',script_content_item
				deleted_function_list.append(script_content_item)

#目前現存的script function
script_content_list_final = list(set(script_content_list) ^ set(deleted_function_list))


pre_script_content =re.split('def ', old_contents)[0]

#Add pre_script_content
Final_script = pre_script_content

#Add 現存的script function
for i in script_content_list_final:
	Final_script+=i

#Add New function

if new_function:
	for i in new_function:
		new_str = 'def '+str(i)+'() :\n    print "'+str(i)+'"\n    global temp\n\n    return "'+str(i)+'"\n\n\n'

		Final_script+=new_str

#Add del function
if del_function:
	Final_script+=del_area

	if deleted_function_list:
		for i in deleted_function_list:
			Final_script+=i	
	Final_script+=del_area_end


#Write to script.py
with open(current_locate+'/script.py', 'w') as f:
	f.write(str(Final_script))
	


#open merged.py
write_file = open(sys.argv[1]+'/merged.py','r')
merged_str = write_file.read()
merged_str = merged_str.replace(merged_str[merged_str.find('temp={}')+9:merged_str.find('#init parameter')],'\n\n\n\n\n\n\n\n') 

#write Runner.py 
write_file = open('/usr/local/GraphwalkerRunner/lib/Runner.py','w')

write_file.write(merged_str)
write_file.close()
