"""
handling errors with logic
"""
import sys
import pickle
# data = open("sketch.txt")
# # print(data.readline(),end='')
# # print(data.readline(),end='')
# for each_line in data:
#     if not  each_line.find(":") == -1:
#         (role,line_spoken) = each_line.split(":",1 )
#         print(role,end="")
#         print("said: ", end="")
#         print(line_spoken,end="")
#
# data.close()

"""
handling them with try method
"""
man = []
other = []

try:
    data = open("sketch.txt")
    # print(data.readline(),end='')
    # print(data.readline(),end='')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(":",1 )
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.append(line_spoken)
            elif role == "Other Man":
                other.append(line_spoken)

            print(role,end="")
            print("said: ", end="")
            print(line_spoken,end="")
        except ValueError:
            pass
    data.close()

except IOError:
    print("data file missing")

# try :
#     man_file = open('man_data.txt',"w")
#     other_file = open('other_data.txt',"w")
#
#     print(man,file=man_file)
#     print(other,file=other_file)
#
# except IOError:
#     print("File Error")
#
#     man_file.close()
#     other_file.close()
try:
    with open("man_data.txt","wb") as man_file, open("other_data.txt","wb")as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print("File Error:" + str(err))
except pickle.PickleError as perr:
    print("Pickling error"+ str(perr))
print(man_file)
print(other_file)


# def print_lol(the_list , indent = False , level =0, identify=sys.stdout):
#
#     for each_item in the_list:
#         if isinstance(each_item,list):
#             print_lol(each_item,indent,level+1,identify,identify)
#         else:
#             if indent:
#                 for tab_stop in range(level):
#                     print("\t",end=" ",file=identify )
#             print(each_item,file = identify)
#
#
# with open("man_data.txt") as mdf:
#     print_lol(man,identify=man_file)
# with open("other_data.txt") as mdf:
#     print_lol(other,identify=other_file)

"""
exercise pencil *with* 

try: 
    with open("man_data.txt","w") as man_file:
    with open("other_data.txt","w") as other_file:
    
    print(man, file=man_file)
    print(other, other_file)
except IOError as err:
    print("file Error: " + str(err))    
    


"""