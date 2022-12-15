import pymongo


ServerPassword = 'test123'
client = pymongo.MongoClient(f"mongodb+srv://test:{ServerPassword}@test.qk4mnho.mongodb.net/?retryWrites=true&w=majority"
 ,tlsAllowInvalidCertificates=True)

db = client.member_system
collection = db.user