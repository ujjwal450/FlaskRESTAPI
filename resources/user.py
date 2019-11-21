import sqlite3
from flask_restful import reqparse, Resource
from models.user import UserModel





class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',

                        type= str,
                        required = True,
                        help = 'This field cannot be left blank'

                        )
    parser.add_argument('password',

                        type=str,
                        required=True,
                        help='This field cannot be left blank'

                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.search_be_username(data["username"]):
            return {"message": "User already exists"}
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User created successfully"}, 201


