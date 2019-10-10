import json
import tkinter
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import sys
from sys import platform


print(platform)
#linux
if platform == "linux" or platform == "linux2":
	filepath=sys.argv[1]
elif platform == "win32":
	#open browse window
	Tk().withdraw()
	filepath = askopenfilename()
#print(filename)
filename=os.path.basename(filepath)

nameSplit=filename.split("_schema")
f = open(filepath)
#load json to list<dictionaty>
data = json.load(f)
f.close()
namefile=str(nameSplit[0])+".sql"
with open(namefile,"w") as text_file:
	text_file.write("create table "+ nameSplit[0] + "(")
	for i in range(len(data)):
		if i==len(data)-1:
			#print (data[i]["name"] + " " + data[i]["type"])
			if data[i]["type"]=="STRING":
				text_file.write(data[i]["name"] + " " + "TEXT" )
			else:
				text_file.write(data[i]["name"] + " " + data[i]["type"])
		else:
			#print (data[i]["name"] + " " + data[i]["type"] + ",")
			if data[i]["type"]=="STRING":
				text_file.write(data[i]["name"] + " " + "TEXT" + ",")
			else:
				text_file.write(data[i]["name"] + " " + data[i]["type"] + ",")
	text_file.write(");")
#print(data["name"])