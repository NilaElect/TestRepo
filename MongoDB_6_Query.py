import pymongo
try:
    uri="mongodb+srv://root:root@databaseserver.3eska.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    connection = pymongo.MongoClient(uri)
    database = connection["NiDB"]# Database Name
    Collection=database["Racks"] #Collection Name
    print('Connection Success!')
except Exception as error:
    print(error)

try:
    #data = Collection.find(query)
    data = Collection.find().sort("Location")#ascending order
    data = Collection.find().sort("Location",-1)#descending order
    for d in data:
        print(d)

except Exception as error:
    print(error)
