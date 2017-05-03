import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

#print(re.match(r'Love', data))
#print(re.search(r'Kenneth', data))
print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))