# -*- coding: utf-8 -*- 
import sys
from string import Template


fun_list = []
merged_str=''

with open(sys.argv[1]+'/merged.py', 'r') as file:

    for line in file:

        if 'def ' in line:
        	fun_list.append(line[4:-5])
    
all_fun_str = '# -*- coding: utf-8 -*- \n\nglobal temp\ntemp={}\n\n\n'

for i in fun_list:
	
	fun_str = Template('def $LABEL() :\n    print "$LABEL"\n    global temp\n    return "$LABEL"\n\n\n\n')
	
	all_fun_str += fun_str.substitute(LABEL=i)

#write fun file
write_file = open(sys.argv[1]+'/script.py','w')

write_file.write(all_fun_str)
write_file.close()

#open merged.py
write_file = open(sys.argv[1]+'/merged.py','r')
merged_str = write_file.read()
merged_str = merged_str.replace(merged_str[merged_str.find('temp={}')+9:merged_str.find('#init parameter')],'\n\n\n\n\n\n\n\n') 

#write GW.py 
write_file = open('/usr/local/GraphwalkerRunner/lib/Runner.py','w')

write_file.write(merged_str)
write_file.close()
