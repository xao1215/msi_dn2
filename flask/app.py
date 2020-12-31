from flask import Flask, render_template
from redis import Redis
from pymongo import MongoClient
import socket
import os

hostname = socket.gethostname()

app = Flask(__name__)
redis = Redis(host="redis") # port=6379

client = MongoClient(os.environ.get('DB')) 
db = client.containers_list

# db = client["mydb"]
# users.insert_one({"a":1})
# mycol = db["users"]
# item = {"name":"john"}
# mycol.insert_one( item )

def give_count():
    return redis.get("counter")

def insert():
    y = True
    value = 0
    for x in db.containers.find():
        if x["id"] == str(hostname):
            y = False
            value = x["visits"] 
            break

    if y:
        cont = {"id":hostname,"visits":0}
        db.containers.insert_one(cont)
    else:
        current = { "id":hostname }
        new = { "$set": { "visits": value+1 } }
        db.containers.update_one(current, new)

def give_containers():
    uf = db.containers.find();
    return uf

@app.route("/")
def hello():
    redis.incr("counter")
    counter = redis.get("counter").decode("utf8")
    insert()
    # k = client.list_collection_names()
    # lol = lol.decode("utf8")
    return render_template( "index.html" , counter=counter, hostname=hostname, containers=give_containers(), length=give_containers().count())
    # return 'Hello World{}" ..." )
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)