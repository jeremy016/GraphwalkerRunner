
# read file & get fun name & write to file

w_file = open('fun_name.txt','w')

with open('merged.py', 'r') as file:

    for line in file:

        if 'def ' in line:
        	w_file.write(line[4:-5])
        	w_file.write('\n')

w_file.close()
        	
        	
       