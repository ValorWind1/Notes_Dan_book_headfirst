import pickle
import python_book_exercises1

new_man=[]

try:
    with open("man_data.txt", "rb") as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print("File Error:" + str(err))
except pickle.PickleError as perr:
    print("Pickling error:" + str(perr))

python_book_exercises1.print_lol(new_man)

print(new_man[0])
print(new_man[-1])

