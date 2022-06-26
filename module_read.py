data={"files":["info.txt","draft.txt"]}

a={
"Ruslan Vafin": data,
"Rosalia Ibatulina":  data,
"Timur Timegaliev": data,
"Arseniy Skotnikov": data,
"Ruslan Sonkin": data
}

import json

f=open('config.txt',"w+")
f.write(json.dumps(a))
f.close()
