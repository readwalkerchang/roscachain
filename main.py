from userAccount import User
import json
import os
from datetime import datetime
from  blockchain import Blockchain

# create 5 accounts

def writeJson(userDict:dict):
    #1. create a file with user's name
    jsonStr = json.dumps(userDict)
    save_path = 'data'
    file_name = json.loads(jsonStr)['name'] + '.json'
    completeName = os.path.join(save_path, file_name)
    #2. put the account message into the file
    with open(completeName, "w") as f :
        f.write(jsonStr)

def writeJsonBlock(blockdict:dict):
    #1. create a file with user's name
    jsonStr = json.dumps(blockdict)
    save_path = 'data'
    file_name = 'block.json'
    completeName = os.path.join(save_path, file_name)
    #2. put the account message into the file
    with open(completeName, "w") as f :
        f.write(jsonStr)

def createUserDB(userName:str):
    #1. create a file with user's name
    newUser = User(userName).__dict__
    jsonStr = json.dumps(newUser)
    save_path = 'data'
    file_name = json.loads(jsonStr)['name'] + '.json'
    completeName = os.path.join(save_path, file_name)
    #2. put the account message into the file
    with open(completeName, "w") as f :
        f.write(jsonStr)
    return newUser

def sendCurrency(sender:object,receiver:object,amount:int):
     senderBalance = sender['balance'] 
     sender['balance'] = senderBalance - amount
     receiverBalance = receiver['balance'] 
     receiver['balance'] = receiverBalance + amount
     writeJson(sender)
     writeJson(receiver)
     #return transaction data
     dt = datetime.now()
     return "{sender} pay {receiver} {timeStamp}".format(sender = sender['name'] ,receiver = receiver['name'], timeStamp = str(dt))

user1 = createUserDB('Bob')
user2 = createUserDB('Amy')
user3 = createUserDB('Lisa')
user4 = createUserDB('Jason')
user5 = createUserDB('Zoey')
pool = createUserDB('Pool')


listToHash = []


s = Blockchain()
s.addBlock(listToHash)
# s.addBlock(['one','two'])

blockdict = s.head.__dict__

jsonStr = json.dumps(blockdict)
writeJsonBlock(jsonStr)


#Run ROSCA
# for x in range(10):
#     listToHash.append(sendCurrency(user1,pool,10))
#     listToHash.append(sendCurrency(user2,pool,10))
#     listToHash.append(sendCurrency(user3,pool,10))
#     listToHash.append(sendCurrency(user4,pool,10))
#     listToHash.append(sendCurrency(user5,pool,10))
#     print('the ' +str(x)+' meeting')



