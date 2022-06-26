import os, json

f = open('config.txt')
j = json.loads(f.read())
f.close()

dir_students_names = "students/"

for key in j:
    value = (j[key])
    try:
        os.makedirs(dir_students_names + key)
    except:
        print('ERROR')

    files_list = value["files"]

    for file in files_list:
        f = open(dir_students_names + key + "/" + file, "w+")
        if file == "info.txt":
            f.write(key)
        f.close()
