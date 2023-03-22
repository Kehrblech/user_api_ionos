from flask import Flask
from flask_restful import Api, Resource
import random
import zehntausend as profile_rnd

app = Flask(__name__)
api = Api(app)

class User(Resource):

    def get(self, id=0, gender=None, size=None):
        if id > 9999:
            return "Max 10.000 users. Contact us for more information", 404
        if size is not None and size < 1 or size is not None and size > 9999:
            return "Invalid Size! Only Numbers between 1-9999", 404
        if size and gender == None:
            size = min(size, 9999) # max size is 10000
            return random.sample(profile_rnd.user, size), 200
        if id == 0 and gender == None:
            return random.choice(profile_rnd.user), 200
        elif id:
            for user in profile_rnd.user:
                if (user["id"] == id):
                
                    return user, 200
            return "Id/user not found", 404
        elif gender and size==None:
            filtered_users = [user for user in profile_rnd.user if user["gender"] == gender]
            if not filtered_users:
                return "No user found with this gender. |diverse|female|male", 404
            return random.choice(filtered_users), 200    
        elif gender and size:
            filtered_users = [user for user in profile_rnd.user if user["gender"] == gender]
            if not filtered_users:
                return "No user found with this gender. |diverse|female|male", 404
            return filtered_users[:size], 200                
api.add_resource(User, "/user", "/user/", "/user/id=<int:id>", "/user/<string:gender>","/user/size=<int:size>","/user/<string:gender>/size=<int:size>","/user/id=<int:id>/", "/user/<string:gender>/","/user/size=<int:size>/","/user/<string:gender>/size=<int:size>/")

if __name__ == '__main__':
    app.run(debug=True)
