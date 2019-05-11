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

print(james)
print(julie)
print(mikey)
print(sarah)

print("----------------")
"""
sort copied, and in-place 
"""

james2 = sorted(james)
julie2 = sorted(julie)
mikey2 = sorted(mikey)
sarah2 = sorted(sarah)

print(james2)
print(julie2)
print(mikey2)
print(sarah2)

"""
the data sorted is incorrect because the txt files contained different symbols separators such as : - , : , . 
so it's not organize properly 
therefore we are going to create a function so that it converts everything to a period. 

"""
def sanitize(time_string):
    time_string.split(splitter)

    if "-" in time_string:
