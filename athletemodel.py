import pickle
from athlete_List import AthleteList


def txt(textFile):
    try:
        with open(textFile) as file:
            data = file.readline()
        temp = data.strip().split(",")
        return (AthleteList(temp.pop(0),temp.pop(0),temp))   # matches with the 3 arguments above us at athelte , name , dob, times
    except IOError as err:
        print("File Error:" + str(err))

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = txt(each_file)   # take each file , turn it into an athelte list + add the list data to dict
        all_athletes[ath.name]=ath # athele's names are used as keys in the dict
    try:
        with open("athletes.pickle","wb") as athf: # wb = writing to a pickle
            pickle.dump(all_athletes,athf) # save the entire dict of atheleLists to a pickle
    except IOError as err:
        print("File Error(put_and_store):" + str(err))
    return (all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open("athletes.pickle","rb") as athf: # reading from a pickle (bytes)
            all_athletes=pickle.load(athf) # reading entire pickle into the dict
    except IOError as err:
        print("File Error (get_from_store):" + str(err))
    return(all_athletes)


# list of files being turn by our function put_to_store into dict stored in a pickle.
the_files = ["sarah2.txt","james2.txt","mikey2.txt","julie2.txt"]
data = put_to_store(the_files)
print(data)

# displaying existing data inside th edict to display athelte's name, and birth.
for each_athl in data:
    print(data[each_athl].name + " "+ data[each_athl].DOB)

# loading pickle data into another dict , and displaying the data that we want.

data_copy = get_from_store()
for i in data_copy:
    print(data_copy[i].name+" "+data_copy[i].DOB)
