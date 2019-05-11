"""
exercise #2
"""
movies = ["the holy grail",1975,"terry jones",91,
            ["graham chapman", [ "michaels palin","john cleese","terry golliam", "erick idle","terry jones"]]]
#
# for each_item in movies:
#     if isinstance(each_item,list):
#         for nested_item in each_item:
#                 if isinstance(nested_item,list):
#                     for deeper_item in nested_item:
#                         print(deeper_item)
#                 else:
#                     print(nested_item)
#     else:
#         print(each_item)

"""
writing ex 1 writing a function of teh code above 
"""
# def print_lol(the_list):
#     for each_item in the_list:
#         if isinstance(each_item,list):
#             print_lol(each_item)
#         else:
#             print(each_item)
# print_lol(movies)

"""
ex2 added range argument for indentention functionality
"""
def print_lol(the_list,indent= True ,level=0):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='')
            print(each_item)

print_lol(movies,True,0)
