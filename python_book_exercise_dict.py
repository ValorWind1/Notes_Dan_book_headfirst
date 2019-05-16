"""
modifief so inside the txt function it automatically buils a dict
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



def txt(textFile):
    try:
        with open(textFile) as file:
            data = file.readline()
        temp = data.strip().split(",")
        return({"Name" : temp.pop(0),"DOB" : temp.pop(0),"Time":str(sorted(set([sanitize(i) for i in temp]))[0:3])})


    except IOError as err:
        print("File Error:" + str(err))


sarah = txt('sarah2.txt')

print(sarah["Name"]+"fastest times are:"+sarah["Time"])


