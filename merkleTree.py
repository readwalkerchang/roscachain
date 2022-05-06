import hashlib

class MerkleTree:
    def __init__(self):
        # self.inputList = []
        self.branchList = []

    def hash(self, val: str)-> str:
        return hashlib.sha256(val.encode("utf-8")).hexdigest()
    
    def createBranch(self, left,right)-> str:
        return self.hash(self.hash(left)+self.hash(right))
    
    def makeBranch(self, inputList:list)-> list:
        branchList = []
        while(len(inputList) > 0):
            if len(inputList) == 1:
                evenInput = inputList.pop(0)
                left, right = evenInput, evenInput
                branchList.append(self.createBranch(left,right))
            else:
                left = inputList.pop(0)
                right = inputList.pop(0)
                branchList.append(self.createBranch(left,right))
        return branchList
    
    def buildTree(self,inputList)-> str:
        branchList = []
        while(len(branchList) != 1):
            branchList = self.makeBranch(inputList)
            if len(inputList) == 0 &  len(branchList) != 1:
                inputList = branchList
        return branchList[0]

        



listToHash = ['hello','world']
newMerkleTree = MerkleTree()
print(newMerkleTree.buildTree(listToHash))