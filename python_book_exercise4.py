with open("james.txt") as james_file : # open the file
    data = james_file.readline()   # read line of data
james = data.strip().split(",")

with open("julie.txt" ) as julie_file:
    data = julie_file.readline()
julie = data.strip().split(",")

with open("mikey.txt") as mikey_file:
    data = mikey_file.readline()
mikey = data.strip().split(",")

with open("sarah.txt") as sarah_file:
    data = sarah_file.readline()
sarah = data.strip().split(",")
#
# print(james)
# print(julie)
# print(mikey)
# print(sarah)
#
# print("----------------")
"""
sort copied, and in-place 
"""
#
# james2 = sorted(james)
# julie2 = sorted(julie)
# mikey2 = sorted(mikey)
# sarah2 = sorted(sarah)
#
# print(james2)
# print(julie2)
# print(mikey2)
# print(sarah2)

"""
the data sorted is incorrect because the txt files contained different symbols separators such as : - , : , . 
so it's not organize properly 
therefore we are going to create a function so that it converts everything to a period. 

"""
def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins+"."+secs)

james1 = []
julie1 = []
mikey1 = []
sarah1 = []


for i in james:
    james1.append(sanitize(i))
for i in julie:
    julie1.append(sanitize(i))
for i in mikey:
    mikey1.append(sanitize(i))
for i in sarah:
    sarah1.append(sanitize(i))

print(sorted(james1))
print(sorted(julie1))
print(sorted(mikey1))
print(sorted(sarah1))

"""
THE SAME BUT EASIER USING LIST COMPREHENSION 
"""
print("----------------------list comprehension---------------------")
james2 = sorted([sanitize(i) for i in james])
julie2 = sorted([sanitize(i) for i in julie])
mikey2 = sorted([sanitize(i) for i in mikey])
sarah2 = sorted([sanitize(i) for i in sarah])

print(sorted(james2))
print(sorted(julie2))
print(sorted(mikey2))
print(sorted(sarah2))

"""
Sorting the first 3 
"""
print("--------------------- deletes duplicate data, and first 3 values ----------------")

unique_james=[]
unique_julie=[]
unique_mikey=[]
unique_sarah=[]

for i in james2:
    if i not in unique_james:
        unique_james.append(i)
for i in julie2:
    if i not in unique_julie:
        unique_julie.append(i)
for i in mikey2:
    if i not in unique_mikey:
        unique_mikey.append(i)
for i in sarah2:
    if i not in unique_sarah:
        unique_sarah.append(i)
# print(unique_james)
# print(unique_julie)
# print(unique_mikey)
# print(unique_sarah)

print(unique_james[0:3])
print(unique_julie[0:3])
print(unique_mikey[0:3])
print(unique_sarah[0:3])

"""
Getting rid of duplicates by using SETS 

"""


