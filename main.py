import userAccount
import json
import os

#create 5 accounts

save_path = 'data'
file_name = 'new_file.json'
completeName = os.path.join(save_path, file_name)
print(completeName)

with open(completeName, "w") as f :
    print("The json file is created")   