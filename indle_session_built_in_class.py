class NamedList(list):
    def __init__(self,a_name):
        list.__init__([])
        self.name= a_name

johnny = NamedList("John Paul Jones")
print(type(johnny))
# print(dir(johnny))
"""
dir = return the list of attributes and methods of any object. 

"""

johnny.append("bass player ")
johnny.extend(["composer","arranger","musician"])
print(johnny)
print(johnny.name)

for attr in johnny:
    print(johnny.name + " is a " + attr + ".")