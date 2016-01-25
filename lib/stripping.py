# -*- coding: utf-8 -*- 
import sys,os,re
from string import Template


fun_list = []
script_fun_list = []

merged_str=''

#read graphml function
with open(sys.argv[1]+'/merged.py', 'r') as file:

    for line in file:

        if 'def ' in line:

        	fun_list.append(line[4:line.find('()')])

#read script function
if os.path.exists(sys.argv[1]+'/script.py'):

	with open(sys.argv[1]+'/script.py', 'r') as file:

	    for line in file:

	        if 'def ' in line :
	        	
	        	script_fun_list.append(line[4:line.find('()')])


	all_fun_str = '\n\n'
else:

	all_fun_str = '# -*- coding: utf-8 -*- \n\nglobal temp\ntemp={}\n\n\n'



difference_sets =  list(set(fun_list) ^ set(script_fun_list))
intersection = list(set(fun_list) & set(script_fun_list))

new_function = list(set(fun_list) ^ set(intersection))

del_function = list(set(script_fun_list) ^ set(intersection))


#def func
if os.path.exists(sys.argv[1]+'/script.py'):
	removed_func_str = ''
	with open(sys.argv[1]+'/script.py', 'r') as file:

		temp = file.read().split('def')
		
		for i in temp:
			
			if i[1:i.find('()')] in del_function:
				
				temp.remove(i)


		removed_func_str =  'def'.join(temp)

else:


	removed_func_str = ''
	
#write fun file
write_file = open(sys.argv[1]+'/script.py','w')

write_file.write(removed_func_str)
write_file.close()		


#add new func
for i in new_function:
	
	fun_str = Template('def $LABEL() :\n    print "$LABEL"\n    global temp\n    return "$LABEL"\n\n\n\n')
	
	all_fun_str += fun_str.substitute(LABEL=i)

#write fun file
write_file = open(sys.argv[1]+'/script.py','a')

write_file.write(all_fun_str)
write_file.close()


#open merged.py
write_file = open(sys.argv[1]+'/merged.py','r')
merged_str = write_file.read()
merged_str = merged_str.replace(merged_str[merged_str.find('temp={}')+9:merged_str.find('#init parameter')],'\n\n\n\n\n\n\n\n') 

#write Runner.py 
write_file = open('/usr/local/GraphwalkerRunner/lib/Runner.py','w')

write_file.write(merged_str)
write_file.close()
