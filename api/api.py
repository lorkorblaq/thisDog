from flask import Flask, request, jsonify, render_template, Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Userz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return {"name":self.name, "email":self.email}


class Dogz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    aggression = db.Column(db.Integer, nullable=False)
    intel = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Dog(name = {self.name}, breed = {self.breed}, aggression = {self.aggression}, intel = {self.intel})"

class Bidder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=True)
    id_user = db.Column(db.Integer, ForeignKey("userz.id"), nullable=False)
    user = relationship("Userz", backref="bids", foreign_keys=[id_user])
    id_dog = db.Column(db.Integer, ForeignKey('dogz.id'), nullable=False)
    dog = relationship("Dogz", backref="bids", foreign_keys=[id_dog])
    initial_price = db.Column(db.Integer, nullable=True)
    last_price = db.Column(db.Integer, nullable=True)
    current_price = db.Column(db.Integer, nullable=False)
    sold = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return f"Bidder(id_user = {self.id_user}, id_dog = {self.id_dog}, initial_price = {self.initial_price}, last_price = {self.last_price}, current_price = {self.current_price}, sold = {self.sold})"
# db.create_all()


user_parser = reqparse.RequestParser()
user_parser.add_argument("user_id", type=int, help="user_id is required", required=True)
user_parser.add_argument("name", type=str, help="user_Name is required", 
required=True)
user_parser.add_argument("email", type=str, help="Email is required", 
required=True)
user_parser.add_argument("password", type=str, help="Password is required", required=True)


bid_parser = reqparse.RequestParser()
bid_parser.add_argument("dog_id", type=int, help="id of DOg is required", required=True)
bid_parser.add_argument("price", type=int, help="Price of the bid is required", required=True)

resource_fields_bid = {
    'id': fields.Integer,
    'created_at': fields.DateTime,
    'id_user': fields.Integer,
    'id_dog': fields.Integer,
    'initial_price': fields.Integer,
    'last_price': fields.Integer,
    'current_price': fields.Integer,
    'sold': fields.Boolean
}
resource_fields_dogs = {
    'id': fields.Integer,
    'name': fields.String,
    'image': fields.String,
    'breed': fields.String,
    'aggression': fields.Integer,
    'intel': fields.Integer
}
resource_fields_users = {
    'user_id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'password': fields.String
}


class User(Resource): 
    # @marshal_with(resource_fields_users)
    def post(self, user_id):
        args = user_parser.parse_args()
        user = Userz(id=args["user_id"], name=args["name"], email=args["email"], password=args["password"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created successfully", "user": user.name, "email": user.email})


class Get_user(Resource):
    def get(self, user_id):
        result = Userz.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User not found")
        return jsonify({"name": result.name, "email": result.email})


class Dog(Resource):
    @marshal_with(resource_fields_dogs)
    def get(self, dog_id):
        result = Dogz.query.filter_by(id=dog_id).first()
        return jsonify({"name": result.name, "breed": result.breed, "aggression":result.aggression, "intel": result.intel}) 


class Get_bid(Resource):
    @marshal_with(resource_fields_bid)
    def get(self, bid_id):
        return 
class Bid(Resource):
    @marshal_with(resource_fields_bid)
    def post(self, user_id):
        args = bid_parser.parse_args()
        bid = Bidder()
        db.session.commit()
        # Do something with the bid information
        return jsonify({"message": f"Bid for user {user_id} received. Dog ID: {args['dog_id']}, Price: {args['price']}"})

    def put(self, user_id):
        if 'price' in request.form:
            args = bid_parser.parse_args(req=request)
            price = args['price']
            # Do something with the updated bid information
            return jsonify({"message": f"Updated bid for user {user_id}. New price: {price}"})
        else:
            return jsonify({"error": "Price not provided in the request"})


# class dogsOnBid(Resource):
    # def get(self):
        # if dogs_on_bid:
            # return jsonify(dogs_on_bid)
        # else:
            # return jsonify({"message": "No dogs on bid"})


api.add_resource(User, "/api/user/<int:user_id>/")
api.add_resource(Get_user, "/api/user/<int:user_id>/")
api.add_resource(Dog, "/api/dog/<int:dog_id>/")
# api.add_resource(breeds, "api/<breeds>")
api.add_resource(Get_bid, "/api/bid/<int:bid_id>")
api.add_resource(Bid, "/api/bid/")

# api.add_resource(dogsOnBid, "/api/dogsOnBids")


if __name__ == "__main__":
    app.run(debug=True)
