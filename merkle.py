listToHash = ['hello','world','hello','world']
branchList = []

def CreateBranch(left,right):
    return hash(hash(left)+hash(right))

def MakeBranch(inputList:list):
    while(len(listToHash) > 0):
        left = inputList.pop(0)
        right = inputList.pop(0)
        branchList.append(CreateBranch(left,right))

        
def BuildTree(inputList:list):
    branchList = []
    inputList = inputList
    while(len(branchList) != 1):
        MakeBranch(inputList)
        # if len(listToHash) == 0 &  len(branchList) != 1:
        #     branchList = []
        #     inputList = branchList

print(BuildTree(listToHash))