
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.DOB= a_dob
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])
#
# def txt(textFile):
#     try:
#         with open(textFile) as file:
#             data = file.readline()
#         temp = data.strip().split(",")
#         return (AthleteList(temp.pop(0),temp.pop(0),temp))   # matches with the 3 arguments above us at athelte , name , dob, times
#     except IOError as err:
#         print("File Error:" + str(err))

def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins+"."+secs)

# sarah = txt("sarah2.txt")
# julie = txt("julie2.txt")
# james = txt("james2.txt")
# mikey = txt("mikey2.txt")
#
#
# print(james.name+ " fastest times are: " + str(james.top3()))
# print(sarah.name + " fastest times are : "+ str(sarah.top3()))
# print(julie.name+ " fastest times are: " + str(julie.top3()))
# print(mikey.name + " fastest times are : "+ str(mikey.top3()))