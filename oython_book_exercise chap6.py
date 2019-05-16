def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins+"."+secs)



def txt(textFile):
    try:
        with open(textFile) as file:
            data = file.readline()
        return(data.strip().split(","))

    except IOError as err:
        print("File Error:" + str(err))

"""
Returning txt sorted, cleaned data but with pop , the name and dob that was included this time in the new txt file 

"""
# sarah = txt('sarah2.txt')

# (sarah_name,sarah_dob) = sarah.pop(0), sarah.pop(0)
#
#
# print(sarah_name + "'s fastest times are: "+str(sorted(set([sanitize(i) for i in sarah]))[0:3]))
"""
Sarah txt file USING DICT 

"""

sarah = txt('sarah2.txt')
sarah_dict = {}
sarah_dict["Name"] = sarah.pop(0)
sarah_dict["DOB"] = sarah.pop(0)
sarah_dict["Time"] = sarah

print(sarah_dict["Name"]+" fastest times are : "+ str(sorted(set([sanitize(i) for i in sarah_dict["Time"]]))[0:3]))
print( "Date of Birth : "+ sarah_dict["DOB"])