from helper import *
from datetime import *

class User:
    def __init__(self,name,trustValue):
        self.name = name
        self.trustValue = trustValue
        self.address = ''
        self.trustValue = 0
        self.balance = 6000
        
        
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
    
    newPool = createPoolDB()
    for x in range(meetingTimes):
        print('the ' +str(x+1)+' meeting')
        # findWinner()
        #print('the ' winner is meeting')
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
        
# def findWinner():
#     return winner

# def verifyTrustvalue():
#     return none