import hashlib

listToHash = ['hello','world','hello','world']
branchList = []

def hash(val: str)-> str:
    return hashlib.sha256(val.encode("utf-8")).hexdigest()

def CreateBranch(left,right):
    return hash(hash(left)+hash(right))

def MakeBranch(inputList:list):
    branchList = []
    while(len(inputList) > 0):
        left = inputList.pop(0)
        right = inputList.pop(0)
        branchList.append(CreateBranch(left,right))
    return branchList

        
def BuildTree(inputList:list):
    branchList = []
    inputList = inputList
    while(len(branchList) != 1):
        branchList = MakeBranch(inputList)
        if len(inputList) == 0 &  len(branchList) != 1:
            inputList = branchList
    return branchList

print(BuildTree(listToHash))