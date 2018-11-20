import pymongo
client=pymongo.MongoClient()
db=client["mylib"]
collection=db["login"]
Username=input("Enter Username :")
Password=input("Enter Password :")
for x in collection.find({},{"Username":1,"Password":1}):
	Username=str(x["Username"])
	Password=int(x["Password"])
if Username==Username and Password==Password:
	    print("Login successfully")
else:
            print("login failed")
