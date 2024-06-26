
from flask import Flask, request
from database import db
# from database.checkDbConnection import check_db_connection
from flask_cors import CORS
from models.User import User
from models.Signature import Signature
from models.DocumentStatus import DocumentStatus
from models.Document import Document
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)
CORS(app)

# app.config.from_object(dbconfig.Configuration)

db.database.connect()
db.database.create_tables([User, Signature, DocumentStatus, Document])


# app.register_blueprint(user_api.userRoutes, url_prefix="/api/user")



@app.get("/")
def hello():
    return {"message": "Hello World", "status": True}


@app.post("/")
def adduser():
    data = request.get_json()
    User.create(**data)
    return {"message": "created successfully", "status": True}


@app.post("/sign")
def addsign():
    data = request.get_json()
    # data.user_id = UUID(data.user_id)
    Signature.create(**data)
    return {"message": "created successfully", "status": True}

@app.get("/alluser")
def alluser():
    users = User.select()
    user_list = list(users)
    user_dict = User.to_dict(user_list)
    return user_dict

@app.get("/allsign")
def allsign():
    users = Signature.select(User.id, User.username).join(User).dicts()
    user_list = list(users)
    # user_dict = Signature.to_dict(users)
    return user_list



@app.get("/sign")
def getsign():
    sign = Signature.select(Signature.id, Signature.signature_name, Signature.initial_name, User.id,
                            User.username, User.fullname).join(User).get()
    # sign_list = list(sign)
    sign_dict = Signature.to_dict(sign)
    return sign_dict


# Remove the if __name__ == '__main__' block
if __name__ == '__main__':
    app.run(debug=True, port=8080)

