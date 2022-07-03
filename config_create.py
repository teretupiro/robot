
import json,os
#from module_read import *
from robot import file

#listfiles=os.listdir(path='students')
dirs=[d for d in os.listdir('students')
      if os.path.isdir(os.path.join('students',d))]


students_dict={}
for i in range(len(dirs)):
    files = [d for d in os.listdir('students/'+dirs[i])
             if os.path.isfile(os.path.join('students/'+dirs[i], d))]
    #TODO: записывать из файла inf.txt в словарь
    d={"files":files,'info':{}}
    students_dict.update([(dirs[i],d)])

f=open("config_2.txt","w+")
f.write(json.dumps(students_dict))
f.close


def parse(line:str):

    key=line.split(':')[0]
    value=line.split(':')[1]
    value=value.replace(" ", "")

    return key,value






