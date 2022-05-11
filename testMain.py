from main import writeJson,createUserDB,sendCurrency

user1 = createUserDB('Bob')
user2 = createUserDB('Amy')
user3 = createUserDB('Lisa')
user4 = createUserDB('Jason')
user5 = createUserDB('Zoey')


listToHash = []
listToHash.append(sendCurrency(user1,user2,50))
listToHash.append(sendCurrency(user2,user3,50))
listToHash.append(sendCurrency(user3,user4,50))
print(listToHash)