import json
import os

def objToJson(fn):
    def wrapped(args):
        with open(fn(args)[0], "w") as f :
            f.write(fn(args)[1])
        return 
    return wrapped

@objToJson
def writeJsonUser(userDict:dict):
    #1. create a file with user's name
    jsonStr = json.dumps(userDict)
    save_path = 'data'
    file_name = json.loads(jsonStr)['name'] + '.json'
    completeName = os.path.join(save_path, file_name)
    return completeName,jsonStr

@objToJson
def writeJsonBlock(blockdict:dict):
    #1. create a file with user's name
    jsonStr = json.dumps(blockdict, indent=4 )
    save_path = 'data'
    file_name = 'block.json'
    completeName = os.path.join(save_path, file_name)
    return completeName,jsonStr