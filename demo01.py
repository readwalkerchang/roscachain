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
OriginalTrust = "Original trust values:\n{0}\n{1}\n{2}\n{3}\n{4}\n".format(data1[101], data1[102],data1[103],data1[104],data1[105])


userlist = [user1, user2, user3, user4, user5]  
runROSCA(5,1000,userlist)

print(OriginalTrust)