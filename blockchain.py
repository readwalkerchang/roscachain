from merkleTree import MerkleTree 

class Block:
    def __init__(self, next):
        self.block = {}
        self.transactions = ()
        self.next = next
        self.rootHash = ''

class Blockchain:
    def __init__(self):
        self.head = None
       
#make block to be a dict and add block to a nested dict
    def addBlock(self, transactions):
        transactionsToAdd = tuple(transactions)
        newMerkleTree = MerkleTree()
        root = newMerkleTree.buildTree(transactions)
        if not self.head:
            NewBlock = Block(None)
            NewBlock.transactions = transactionsToAdd
            NewBlock.rootHash = root
            self.head = NewBlock
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        NewBlock = Block(None)
        NewBlock.transactions = transactions
        NewBlock.rootHash =root
        curr.next = NewBlock

    def get_last_node(self):
        n = self.head
        while(n.next != None):
            n = n.next
        return n.transactions

    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        while n != None:
            print(n.rootHash[0:5]+'...', end = " => ")
            n = n.next
        print()

    # def writeBlock(self):

#text codes
# newBlock = Block(['001','002'],'hiufahkfue3y987493',None)
# print(newBlock.transactions)
# listToHash = ['001','002']
# s = Blockchain()
# s.addBlock(listToHash)
# s.addBlock(listToHash)
#the list to hash will be disappaer
# blockdict = s.head
# print(blockdict.transactions)