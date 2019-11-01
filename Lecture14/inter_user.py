#!/user/bin/python3

name = str(input("What is your name?\n"))
age = str(input("How ald are you?\n"))
#gender = str(input("What is your gender? Male or Female\n"))
color = str(input("What is your favourite colour?\n")).lower()
python = str(input("Do you like Python? y/n\n")).lower()
world = str(input("The world is flat: True or False?\n")).lower()

mydict = {'name':name, 'age':age,'color':color,'python':python,'world':world}

def comments(dictio):
	print(dictio['name']+"'s favourite color is "+dictio['color']+" and "+dictio['name']+" is "+dictio['age']+" years old")
	if python == "yes":
		print(dictio['name']+" likes Python and thinks that world is ", end = '')
	elif python == "no":
		print(dictio['name']+" does not like Python and thinks that world is ", end = '')
	if world == "true":
		print("flat.")
	elif world == "false":
		print("not flat.")

comments(mydict)
