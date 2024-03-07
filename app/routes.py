from flask import Flask

app = Flask(__name__) #Creating an instancenof Flask into app (now an object)

@app.get("/") #Flask decorator that maps routes to view functions
def index(): 
    me={ # python dictionary (key-value pairs)
        "first_name":"Marco",
        "last_name":"Leon",
        "hobbies":"Volleyball",
        "online": True
    }
    return me