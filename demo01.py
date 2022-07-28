from userAccount import *
import json
import os
from datetime import datetime
from  blockchain import Blockchain
import numpy as np
data1 = np.loadtxt("data.csv")



user1 = createUserDB('Bob',data1[101])
user2 = createUserDB('Amy',data1[102])
user3 = createUserDB('Lisa',data1[103])
user4 = createUserDB('Jason',data1[104])
user5 = createUserDB('Zoey',data1[105])
pool = createPoolDB()


# listToHash1 = []
# listToHash1.append(sendCurrency(user1,user2,10))
# listToHash1.append(sendCurrency(user2,user1,10))
# listToHash1.append(sendCurrency(user3,user4,10))
# listToHash1.append(sendCurrency(user4,user3,10))
# listToHash1.append(sendCurrency(user5,user1,10))
# listToHash1.append(sendCurrency(user1,user5,10))

# s = Blockchain()
# s.addBlock(listToHash1)
# blockdict = s.head.__dict__
# writeJsonBlock(blockdict)
# print(blockdict)