from helper import *
class User:
    def __init__(self,name):
        self.name = name
        self.address = ''
        self.trustValue = 0
        self.balance = 50
        
        
class Pool:
    def __init__(self):
        self.name = 'pool'
        self.address = ''
        self.balance = 0
        
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