"""'
classes python exercise
"""

"""
every class has a special method call __init__() , allows control how objects are initialized.
 
"""

class Athlete:

    def __init__(self,a_name,a_dob=None,a_times=[]):
        # the code to initialize a "athlete" object.
        self.name =a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return str(sorted(set([sanitize(i) for i in self.times]))[0:3])

    def add_time(self,time_string):
        self.times.append(time_string)

    def add_times(self,list_of_times):
        self.times.extend(list_of_times)


def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + "." + secs)


def txt(textFile):
    try:
        with open(textFile) as file:
            data = file.readline()
        temp = data.strip().split(",")
        return (Athlete(temp.pop(0),temp.pop(0),temp))   # matches with the 3 arguments above us at athelte , name , dob, times
    except IOError as err:
        print("File Error:" + str(err))



james = txt("james2.txt")
print(james.name + " fastest times are : " + str(james.top3()))

"""
new taste case (athlete) - named vera 
"""
vera = Athlete("vera vi")
vera.add_time("1.31")
print ( vera.top3())

vera.add_times(["2.22","1-21","2:22"])
print(vera.top3())

# sarah = Athlete("Sarah Sweeney", "2002-6-17", ["2:58","2..58","1.56"])
# james = Athlete("James Jones")

# print (type(sarah))   # confirming that both sarah and james are indeed part of Atheltes
# print(type(james))

# print(sarah.times)
# print(sarah.name)
# print(sarah.dob)

