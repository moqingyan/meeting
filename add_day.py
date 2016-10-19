#a script to insert date info to the html code

import os


path = os.path.abspath(__file__+'/../')
target = os.path.join(path, "create_event.html")

#create the string to insert
string_to_insert = ""
for i in range(1,31):
	string_to_insert = string_to_insert + ("\t"+ "<li>" + str(i) + "</li>\n")
print(string_to_insert)

#modify the file
with open (target, "r+") as modify_file:
    data = modify_file.read()
    print(type(data))
    pattern = "ToChange"
    data = data.replace(pattern, string_to_insert);
    modify_file.write(data)
modify_file.close()
