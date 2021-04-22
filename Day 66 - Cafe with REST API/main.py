from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Create a new dictionary entry
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random', methods=['GET'])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())
    # return jsonify(
    #     cafe={
    #         # Omit the id from the response
    #         # 'id': random_cafe.id,
    #         'name': random_cafe.name,
    #         'map_url': random_cafe.map_url,
    #         'location': random_cafe.location,

    #         # Make some properties as sub-category
    #         "amenities": {
    #             'seats': random_cafe.seats,
    #             'has_toilet': random_cafe.has_toilet,
    #             'has_wifi': random_cafe.has_wifi,
    #             'has_sockets': random_cafe.has_sockets,
    #             'can_take_calls': random_cafe.can_take_calls,
    #             'coffee_price': random_cafe.coffee_price,
    #         }
    #     }
    # )


@app.route('/all')
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route('/search')
def get_cafe_at_location():
    query_location = request.args.get('loc')
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={'Not Found': 'Sorry, we do not have a cafe at that location'})


if __name__ == '__main__':
    app.run(debug=True)
