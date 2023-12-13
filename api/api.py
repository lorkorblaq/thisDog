from flask import Flask, request, jsonify, render_template, Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
# from thisDog.models.engine import db

# db = db()


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Userz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return {"name": self.name, "email": self.email}


class Dogz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    aggression = db.Column(db.Integer, nullable=False)
    intel = db.Column(db.Integer, nullable=False)
    descrip = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Dog(name = {self.name}, descrip = {self.descrip}, breed = {self.breed}, aggression = {self.aggression}, intel = {self.intel})"

class Bidder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    id_user = db.Column(db.Integer, ForeignKey("userz.id"), nullable=False)
    user = relationship("Userz", backref="bids", foreign_keys=[id_user])
    id_dog = db.Column(db.Integer, ForeignKey('dogz.id'), nullable=False)
    dog = relationship("Dogz", backref="bids", foreign_keys=[id_dog])
    initial_price = db.Column(db.Integer, nullable=True)
    last_price = db.Column(db.Integer, nullable=True)
    current_price = db.Column(db.Integer, nullable=False)
    sold = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Bidder(id_user = {self.id_user}, id_dog = {self.id_dog}, initial_price = {self.initial_price}, last_price = {self.last_price}, current_price = {self.current_price}, sold = {self.sold})"
#db.create_all()


user_parser = reqparse.RequestParser()
user_parser.add_argument("name", type=str, help="user_Name is required", 
required=True)
user_parser.add_argument("email", type=str, help="Email is required", 
required=True)
user_parser.add_argument("password", type=str, help="Password is required", required=True)

dog_parser = reqparse.RequestParser()
dog_parser.add_argument("name", type=str, help="Name needed", required=True)
dog_parser.add_argument("image", type=str, help="Image needed", required=True)
dog_parser.add_argument("descrip", type=str, help="Description needed", required=True)
dog_parser.add_argument("breed", type=str, help="Breed needed", required=True)
dog_parser.add_argument("aggression", type=int, help="Aggresion level needed", required=True)
dog_parser.add_argument("intel", type=int, help="Intelligence level needed", required=True)



bid_parser = reqparse.RequestParser()
bid_parser.add_argument("id_user", type=int, help="User id of the bid is required", required=True)
bid_parser.add_argument("id_dog", type=int, help="Dog id of the bid is required", required=True)
bid_parser.add_argument("current_price", type=float, help="Current price of the bid is required", required=True)



resource_fields_users = {
    'name': fields.String,
    'email': fields.String,
    'password': fields.String
}

resource_fields_dogs = {
    'name': fields.String,
    'image': fields.String,
    'descrip': fields.String,
    'breed': fields.String,
    'aggression': fields.Integer,
    'intel': fields.Integer
}

resource_fields_bid = {
    'id_user': fields.Integer,
    'id_dog': fields.Integer,
    'current_price': fields.Integer,
}

#user related api
class User(Resource):
    def get(self, user_id):
        result = Userz.query.filter_by(id=user_id).first()
        #result = db.Userz.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User not found")
        return jsonify({"name": result.name, "email": result.email})
    
    def put(self, user_id):
        result = Userz.query.filter_by(id=user_id).first()
        #result = db.Userz.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User not found")
        return jsonify({"name": result.name, "email": result.email})

    def delete(self, user_id):
        result = Userz.query.filter_by(id=user_id).first()
        #result = db.Userz.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="User not found")
        return jsonify({"name": result.name, "email": result.email})


class Users(Resource): 
    # @marshal_with(resource_fields_users)
    def post(self):
        args = user_parser.parse_args()
        if Userz.query.filter_by(email=args['email']).first():
            response = {"message": "Email already exists"}
            return response, 400
        user = Userz(name=args["name"], email=args["email"], password=args["password"])
        #user = db.Userz(name=args["name"], email=args["email"], password=args["password"])
        db.session.add(user)
        db.session.commit()
        response = {
            "message": "User created successfully", 
            "userid":user.id, 
            "user": user.name, 
            "email": user.email}
        return response, 201

    def get(self):
        results = Userz.query.all()
        #result = db.Userz.query.all()
        if not results:
            abort(404, message="User not found")
        user_list = []
        for result in results:
            user_info = {
                    "name":result.name,
                    "email":result.email,
                    "password":result.password
            }
            user_list.append(user_info)
        return jsonify({"users":user_list})

#dog related api
class Dog(Resource): 
    def get(self, dog_id):
        return jsonify({"message": "Dog created successfully"})
    # @marshal_with(resource_fields_users)
     
    

class Dogs(Resource):
    # @marshal_with(resource_fields_dogs)
     def post(self):
        args = dog_parser.parse_args()
        dog = Dogz(name=args["name"], image=args["image"], descrip=args["descrip"], breed=args["breed"], aggression=args["aggression"], intel= args["intel"])
        #dog = db.Dogz(name=args["name"], image=args["image"], breed=args["breed"], aggression=args["aggression"], intel= args["intel"])
        db.session.add(dog)
        db.session.commit()
        response = {
            "message": "Dog created successfully", 
            "dog Id": dog.id, 
            "name": dog.name,
            "image": dog.image,
            "descrip": dog.descrip, 
            "breed": dog.breed,
            "aggression": dog.aggression,
            "intel": dog.intel
        }
        return response, 201
    
     def get(self):
        results = Dogz.query.all()
        #results = db.Dogz.query.all()
        dogs_list = []
        for result in results:
            dog_info = {
                    "id":result.id,
                    "name":result.name,
                    "image":result.image,
                    "descrip":result.descrip,
                    "breed":result.breed,
                    "aggression":result.aggression,
                    "intel": result.intel
            }
            dogs_list.append(dog_info)
        return jsonify({"dogs":dogs_list})
  
   
#bid related api
class Create_bid(Resource):
    #@marshal_with(resource_fields_bid)
    def post(self):
        args = bid_parser.parse_args()
        user_id = args['id_user']
        dog_id = args['id_dog']
    
        # Ensure that the provided user and dog IDs exist in the Userz and Dogz tables
        user = Userz.query.get(user_id)
        #user = db.Userz.query.get(user_id)
        dog = Dogz.query.get(dog_id)
        #dog = db.Dogz.query.get(dog_id)


        if not user:
            abort(404, message=f"User with ID {user_id} not found")
        if not dog:
            abort(404, message=f"Dog with ID {dog_id} not found")
        bid = Bidder(
            id_user = user,
            id_dog = dog, 
            initial_price = args["initial_price"], 
            last_price = args["last_price"], 
            current_price = args["current_price"], 
            sold = args["sold"]
        )
        

        db.session.add(bid)
        db.session.commit()


        # Do something with the bid information
        return jsonify({
            "message": f"Bid for user {user_id} received", 
            "User Id": bid.id_user, 
            "Dog id": bid.id_dog, 
            "Price": bid.current_price,
            "sold": bid.sold
        })


    def put(self, user_id):
        if 'price' in request.form:
            args = bid_parser.parse_args(req=request)
            price = args['price']
            # Do something with the updated bid information
            return jsonify({"message": f"Updated bid for user {user_id}. New price: {price}"})
        else:
            return jsonify({"error": "Price not provided in the request"})


class Bids(Resource):
    def post(self):
        try:
            args = bid_parser.parse_args()
            user_id = args['id_user']
            dog_id = args['id_dog']
            current_price = args['current_price']

            # Ensure that the provided user and dog IDs exist in the Userz and Dogz tables
            user = Userz.query.get(user_id)
            #user = db.Userz.query.get(user_id)
            dog = Dogz.query.get(dog_id)
            #dog = db.Dogz.query.get(dog_id)
            bid = Bidder.query.all()
            bid_on_dog = Bidder.query.filter_by(id_dog=dog_id).first()

            if not user:
                abort(404, message=f"User with ID {user_id} not found")
            if not dog:
                abort(404, message=f"Dog with ID {dog_id} not found")

            if not bid_on_dog:
                bid = Bidder(
                    id_user = user_id,
                    id_dog = dog_id, 
                    initial_price = current_price, 
                    last_price = current_price, 
                    current_price = current_price, 
                    sold = False
                )
                db.session.add(bid)
            else:
                bid_on_dog.id_user = user_id
                bid_on_dog.last_price = bid_on_dog.current_price
                bid_on_dog.current_price = current_price
            db.session.commit()
            response = {
                "message": f"Bid for user {user_id} received", 
                "User Id": bid_on_dog.id_user, 
                "Dog id": bid_on_dog.id_dog, 
                "Initial Price": bid_on_dog.initial_price,
                "Last price": bid_on_dog.last_price,
                "current price": bid_on_dog.current_price,
            }
            return response, 201
                # 
        except Exception as e:
            db.session.rollback()
            if not user:
                abort(404, message=f"User with ID {user_id} not found")
            elif not dog:
                abort(404, message=f"Dog with ID {dog_id} not found")

           

        # Do something with the bid information
    # @marshal_with(resource_fields_bid)
    def get(self):
        results = Bidder.query.all()
        bid_list = []
        for result in results:
            bid_info = {
                    "id_user":result.id_user,
                    "id_dog":result.id_dog,
                    "initial_price":result.initial_price,
                    "last_price":result.last_price,
                    "current_price":result.current_price,
                    "sold": result.sold
            }
            bid_list.append(bid_info)
        return jsonify({"bids":bid_list})

    


# class dogsOnBid(Resource):
    # def get(self):
        # if dogs_on_bid:
            # return jsonify(dogs_on_bid)
        # else:
            # return jsonify({"message": "No dogs on bid"})


api.add_resource(User, "/api/user/<int:user_id>")
api.add_resource(Users, "/api/users/")
api.add_resource(Dog, "/api/dog/<int:dog_id>/")
api.add_resource(Dogs, "/api/dogs/")
# api.add_resource(breeds, "api/<breeds>")
api.add_resource(Bids, "/api/bids/")
api.add_resource(Create_bid, "/api/bid/create/")

# api.add_resource(dogsOnBid, "/api/dogsOnBids")


if __name__ == "__main__":
    app.run(port=5000, debug=True)