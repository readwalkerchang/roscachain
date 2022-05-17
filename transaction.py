from userAccount import Pool
import os
from datetime import datetime
from helper import *

# create 5 accounts

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
     writeJsonUser(sender)
     writeJsonUser(receiver)
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
        writeJsonUser(winner)
        print(winner['name']+' has '+str(userList[x]['balance']))