from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    brain_coins = db.Column(db.Integer, default=0)
    avatar = db.Column(db.String(255), default="static/images/avatar1.png")

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    options = db.Column(db.String(255), nullable=False)  # JSON string: "option1,option2,option3,option4"
    correct_answer = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)  # 1 (Easy), 2 (Medium), 3 (Hard)

class UserScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)