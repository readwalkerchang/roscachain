from transaction import *
from userAccount import *
from blockchain import *

#Create a block with transactions and rootHash
user1 = createUserDB('Bob')
user2 = createUserDB('Amy')
user3 = createUserDB('Lisa')
user4 = createUserDB('Jason')
user5 = createUserDB('Zoey')
pool = createPoolDB()


listToHash1 = []
listToHash1.append(sendCurrency(user1,user2,10))
listToHash1.append(sendCurrency(user2,user1,10))
listToHash1.append(sendCurrency(user3,user4,10))
listToHash1.append(sendCurrency(user4,user3,10))
listToHash1.append(sendCurrency(user5,user1,10))
listToHash1.append(sendCurrency(user1,user5,10))

s = Blockchain()
s.addBlock(listToHash1)
blockdict = s.head.__dict__
writeJsonBlock(blockdict)
print(blockdict)


### Run a ROSCA and update trust value

userlist = [user1, user2, user3, user4, user5]
runROSCA(5,10,userlist)