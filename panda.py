import pandas as pd

#df = pd.read_csv("pokemon_data.csv")

# print(df) # prints all the data
# print(df.head(3))   # prints the top 3 rows
# print ( df.tail(3)) # prints the bottom 3 row

"""
Reading data in Pandas 
"""
## READING HEADERS
# print (df.columns)
"""
READ EACH COLUMN
"""
#print(df["Name"][0:5])   # especifying data that I want. in this case
                        # all the names of the pokemon [0:5] especifies the range so from 0 to 5

#print(df[["Name","Type 1","HP"]])   # you can also do multiple columns, and they don't have to be in order
"""
PRINTING EACH ROW 
"""

#print(df.iloc[1])      # Printing a specific row , iloc = integer location
#print(df.iloc[0:4])     # multiple rows
"""
READ SPECIFIC LOCATION (R,C)
"""

# print(df.iloc[2,1])    # [2,1] = [2nd row , position]
"""
ITERATE THROUGH EACH ROW 
"""

# for index , row in df.iterrows():
#     print(index,row["Name"])

"""
FINDIN SPECIFIC ROWS WITH VALUES THAT YOU NEED 
"""
#print(df.loc[df["Type 1"]=="Fire"])

"""
DESCRIBE HIGH LEVEL STATS 
"""
#print(df.describe())

"""
SORTING VALUES 
"""
#print(df.sort_values("Name",ascending=False))   # sortting all the names in desending order

#print(df.sort_values(["Type 1", "HP"],ascending=[1,0]))          # sorting with multiple values [1,0] = first ascending ,and the second one descending

"""
MAKING CHANGES TO THE DATA 
(adding all the values of the stats together)
"""
#df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"]+df["Sp. Def"]+df["Speed"]

# print(df.sort_values("Total",ascending=False))

"""
DROP SPECIFIC COLUMN 

"""
#df=df.drop(columns=["Total"])   # droping the total column up top that we created
# print(df)

"""
DIFFERENT WAY OF ADDING ALL THE COLUMNS (STATS TOGETHER)
"""
#df["Total"] = df.iloc[:,4:10].sum(axis=1) # the : input means all the rows. 4 ( because HP column starts at position 4
#print(df)                                 # SUM METHOD. AXIS if you want to sum horizontaly u NEED TO SPECIFY
                                        # AXIS = 1 HORIZONTALLY , AXIS = 0 VERTICALLY
"""
CHANGING POSITIONS OF COLUMNS 
"""
# cols = list(df.columns.values)
# df= df[cols[0:4]+[cols[-1]]+cols[4:12]]   # -1 = last column
#
# print(df)

"""
SAVING UPDATED DATA TO A FILE 
"""
#df.to_csv("modified.csv",index=False)    # also will delete the indexes , the column all the way to the left

#df.to_excel("modified.xlsx",index=False)  # Saving it as an excel file

# df.to_csv("modified.txt",index=False, sep="\t")   # saving it as a TXT file , SEP = SEPARATION PARAMETER

"""
FILTERING DATA  

"""

#print(df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")])  # multiple conditions , so we will only have grass and posion

"""
python pandas OR  = | 
ex : print(df.loc[(df["Type 1"] == "Grass") | (df["Type 2"] == "Poison")]) 
we replaced the and for the or= |
"""
df = pd.read_csv("modified.csv")
# print(df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)]) # three conditionals

#new_df= df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)] # saving it as a new data frame
# saving this new data frame to a new csv file
# new_df.to_csv("filtered.csv")
#new_df=new_df.reset_index()    # resets the index
#new_df.reset_index(drop=True,inplace=True)   # resets the index but without using a new data frame.
#print(new_df)

"""
FILTERING SPECIFIC WORDS FROM DATA , and FILTERING OUT SPECIFIC WORDS TOO 
"""
#print(df.loc[(df["Name"].str.contains("Mega"))])  # print all the columns with the word Mega

#print(df.loc[(~df["Name"].str.contains("Mega"))])  # gets rid of all Mega words from the data

"""
import re #imports regular expression
"""

#print(df.loc[(df["Type 1"].str.contains("fire|grass",flags=re.I, regex=True))])   # flasgs ignores differences with capitals letters

#print(df.loc[(df["Name"].str.contains("^pi[a-z]*",flags=re.I, regex=True))])   # Getting data tha tyou want. * means one ore more , and ^ means start with pi.

"""
CONDITIONAL CHANGES 
"""

# df.loc[df["Type 1"] == "Fire" , "Type 1"] = "Flamer"    # changin the names in this case fire to flamer
# # # print(df)

# df.loc[df["Type 1"] == "Fire" , "Legendary"] = True      # So you can make all fire type pokemon to legendary
#print(df)

# df.loc[df["Total"] > 500, ["Generation","Legendary"]]  =" Test Value"  # multiple conditions can be modified at the same time
# df.loc[df["Total"] > 500, ["Generation","Legendary"]] =["Test 1","Test 2"] #modified them individually too
# print(df)

"""
AGGREGATE STATISTICS (GROUP BY) function , COOL ANALYSIS STUFF 

"""

#print(df.groupby(["Type 1"]).mean().sort_values("Defense",ascending=False))   # COOL STUFF WE CAN SEE ALL OF THE STATS BROKEN DOWN BY THEIR MEAN

# print(df.groupby(["Type 1"]).sum())     # Sum all of them



#df ["count"] = 1   # you create a count column

# print(df.groupby(["Type 1"]).count()["count"])     # Count all pokemon amount

#print(df.groupby(["Type 1","Type 2"]).count()["count"])    # group by multiple parameters

"""
WORKING WITH LARGE AMOUNTS OF DATA 

"""

# for df in pd.read_csv("modified.csv",chunksize=5):  # 5 rows are being passed at a time.
#     print("CHUNK DATAFRAME")
#     print(df)

new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv("modified.csv",chunksize=5):  # 5 rows are being passed at a time.
    results = df.grouby(["Type 1"]).count()

    new_df = pd.concat([new_df,results])