import hashlib

def hash(val: str)-> str:
    return hashlib.sha256(val.encode("utf-8")).hexdigest()

listToHash = ['hello','world','hello','world']
branchList = []

def CreateBranch(left,right):
    return hash(hash(left)+hash(right))

def BuildTree(inputList:list):
    while(len(inputList) > 0):
        if len(inputList)>1:
            left = inputList.pop(0)
            right = inputList.pop(0)
        branchList.append(CreateBranch(left,right))
        inputList = branchList

    if(len(branchList) == 1):
        return branchList[0]


print(BuildTree(listToHash))