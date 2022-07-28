from helper import *
from datetime import *
import random

class User:
    def __init__(self,name,trustValue):
        self.name = name
        self.trustValue = trustValue
        self.address = ''
        self.balance = 6000
        self.bidingPrice = 0
        
        
class Pool:
    def __init__(self):
        self.name = 'pool'
        self.address = ''
        self.balance = 0
        
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

def createUserDB(userName:str ,trustValue:float):
    #1. create a file with user's name
    newUser = User(userName,trustValue).__dict__
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
    bidingList = userList[1:] #create a list for biding
    roscaUserList = [userList[0]]
    winningState = {"winner": {}, "bidingPrice": 0}
    newPool = createPoolDB()
    for x in range(meetingTimes):
        print('the ' +str(x+1)+' meeting')
        if x > 0 and x < meetingTimes: #excludd first run(no biding)
            roscaUserList = roscaUserList [:x]
            winningState = biding(bidingList)
            bidingList.remove(winningState["winner"])
            roscaUserList.append(winningState["winner"])
        for y in roscaUserList:
            if(roscaUserList[x] != y):
                sendCurrency(y,newPool,amount)
                print('Pay success')
        for z in bidingList:
            if len(bidingList) > 1 :
                sendCurrency(z,newPool,amount - winningState["bidingPrice"])
                print('Pay success ')
        sendCurrency(newPool,roscaUserList[x],newPool['balance']) # send funds to the winner
        print("the winner is: ",roscaUserList[x]["name"])
        #update trust value
        roscaUserList = roscaUserList + bidingList
        updateTrustvalue(roscaUserList)
        print(bidingList)
        print(roscaUserList)
        
def biding(bidinglist):
    pricesToCompare = []
    for x in bidinglist:
        price = random.randint(100,300)
        x["bidingPrice"] = price
        pricesToCompare.append(price)
    Max = max(pricesToCompare)
    maxIndex = pricesToCompare.index(Max)
    winner = bidinglist[maxIndex]
    winningState = {"winner": winner, "bidingPrice": Max}
    return winningState

def updateTrustvalue(roscaUserList):
    trustvalue =  1
    for i in roscaUserList:
        i['trustValue'] += trustvalue
    writeJson(i)