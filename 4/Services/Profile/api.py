from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
import jwt

# Initialize Flask
app = Flask(__name__)
api = Api(app)

user_profiles = []

userProfile_fields = {
    "username": fields.String,
    "description": fields.String
}


class UserProfile(Resource):
    # Initialize Flask's Request Parser and add arguments as in an expected request
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("description", type=str, location="json")
        self.reqparse.add_argument("token", type=str, location="headers")

        super(UserProfile, self).__init__()

    # GET - Returns a single user profile given a matching username
    def get(self, username):
        print(username, len(user_profiles))

        userProfile = None
        for up in user_profiles:
            if up['username'] == username:
                userProfile = up
                break

        if userProfile is None:
            abort(404)  # The user hasn't been found. So we should sent a 404 answer.

        # Otherwise the user profile should be returned.
        return {"userprofile": marshal(userProfile, userProfile_fields)}

    # PUT - Given a username -> update the profile
    def put(self, username):
        args = self.reqparse.parse_args()
        if args["token"] is None:
            abort(401)  # The user is unauthenticated.
        if jwt.decode(args["token"], options={"verify_signature": False})["username"] != username:
            abort(401)  # The user is going to update someone else's profile.

        userProfile = None
        for up in user_profiles:
            if up['username'] == username:
                userProfile = up
                break

        if userProfile is None:
            abort(404)  # The user hasn't been found. So we should sent a 404 answer.

        # Loop Through all the passed agruments (in our current implementation, it would be only the description)
        args = self.reqparse.parse_args()
        for key, value in args.items():
            if value is not None:
                # if the passed value is not null, do the update.
                userProfile[key] = value

        return {"userprofile": marshal(userProfile, userProfile_fields)}


# In the given task, none of the users (or their profiles) would be deleted. So there is no need to define a delete method.


class UserProfileList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("username", type=str, required=False, help="The intended username", location="json")
        self.reqparse.add_argument("description", type=str, required=False, help="The intended user profile", location="json")
        self.reqparse.add_argument("token", type=str, location="headers")

    # Create a new user profile.
    def post(self):
        args = self.reqparse.parse_args()

        print(args)

        if args["token"] is None:
            abort(401)  # The user is unauthenticated.

        if jwt.decode(args["token"], options={"verify_signature": False})["username"] != args["username"]:
            abort(401)  # The user is going to update someone else's profile.

        up = {
            "username": args["username"],
            "description": args["description"]
        }

        user_profiles.append(up)
        return {"userprofile": marshal(up, userProfile_fields)}, 201


api.add_resource(UserProfileList, "/userprofiles")
api.add_resource(UserProfile, "/userprofiles/<string:username>")


@app.route('/is_alive', methods=['GET'])
def is_alive():
    return jsonify({'message': 'Service is alive'}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
