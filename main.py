from userAccount import User
from userAccount import Pool
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
    jsonStr = json.dumps(blockdict, indent=4 )
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

def createPoolDB():
    #1. create a file with user's name
    newPool = Pool().__dict__
    jsonStr = json.dumps(newPool)
    save_path = 'data'
    file_name = json.loads(jsonStr)['name'] + '.json'
    completeName = os.path.join(save_path, file_name)
    #2. put the account message into the file
    with open(completeName, "w") as f :
        f.write(jsonStr)
    return newPool

def sendCurrency(sender:object,receiver:object,amount:int):
     senderBalance = int(sender['balance']) 
     sender['balance'] = senderBalance - amount
     receiverBalance = int(receiver['balance'] )
     receiver['balance'] = receiverBalance + amount
     writeJson(sender)
     writeJson(receiver)
     #return transaction data
     dt = datetime.now()
     return "{sender} pay {receiver} {timeStamp}".format(sender = sender['name'] ,receiver = receiver['name'], timeStamp = str(dt))

def runROSCA(meetingTimes:int, amount:int, userList:list):
    newPool = createPoolDB()
    for x in range(meetingTimes):
        print('the ' +str(x+1)+' meeting')
        for y in userList:
            if sendCurrency(y,newPool,amount):
                print('Pay success ')
        sendCurrency(newPool,userList[x],newPool['balance'])
        #update trust value
        winner = userList[x]
        trustvalue =  (x+1)/10
        winner['trustValue'] += trustvalue
        writeJson(winner)
        print(winner['name']+' has '+str(userList[x]['balance']))


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


### Run a ROSCA and update trust value

userlist = [user1, user2, user3, user4, user5]
runROSCA(5,10,userlist)