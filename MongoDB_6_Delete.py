import pymongo
try:
    uri="mongodb+srv://root:root@databaseserver.3eska.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    connection = pymongo.MongoClient(uri)
    database = connection["NiDB"]
    database = connection["NiDB"]# Database Name
    Collection=database["Racks"] #Collection Name
except Exception as error:
    print(error)

#query={'Rack Name':'AS 02'}

try:
    #Collection.delete_one(query)
    #print('Delete Successful!')

    data=Collection.delete_many({})
    print('Delete Documents: ', data.deleted_count)


except Exception as error:
    print(error)