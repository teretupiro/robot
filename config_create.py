
import json,os


listfiles=os.listdir(path='students')
dirs=[d for d in os.listdir('students')
      if os.path.isdir(os.path.join('students',d))]

students_dict={}
for i in range(len(dirs)):

  students_dict.update([(dirs[i],'empty')])


print(students_dict)