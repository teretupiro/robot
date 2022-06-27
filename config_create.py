
import json,os
from module_read import *
from robot import file

listfiles=os.listdir(path='students')
dirs=[d for d in os.listdir('students')
      if os.path.isdir(os.path.join('students',d))]

students_dict={}
for i in range(len(dirs)):
  students_dict.update([(dirs[i],data)])

f=open("config_2.txt","w+")
f.write(json.dumps(students_dict))
f.close


print(students_dict)