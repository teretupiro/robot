from config_create import parse
file='students3/Ruslan Vafin/info.txt'

f=open(file,encoding='utf-8')
line_list=f.readlines()
f.close()

i=0
for line in line_list:

    if i>0:
        print(line)
        key,value=parse(line)
        print('key=',key,'value=',value)
    i+=1