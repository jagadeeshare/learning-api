from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker
from db import engine
from models import Base, Person

# Create tables (make sure models are imported before this line)
Base.metadata.create_all(engine)

# Session factory: one session per usage
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

app = Flask(__name__)
# If you plan to use Flask's session later, uncomment:
# app.config['SECRET_KEY'] = 'change-this-in-prod'

@app.route("/")
def home():
    return "Server is running"

@app.route("/student", methods=["GET"])
def read_all():
    # Use a distinct name to avoid confusion with flask.session
    with Session() as db_session:
        students = db_session.query(Person).all()
        return jsonify([{"id": s.id, "name": s.name} for s in students]), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)