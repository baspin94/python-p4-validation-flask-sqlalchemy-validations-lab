from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)

    @validates('name')
    def validate_name(self, key, name):
        if len(name) == 0:
            raise ValueError("Name cannot be an empty string.")
        return name
    
    @validates('phone_number')
    def validate_phone(self, key, number):
        if len(number) != 10:
            raise ValueError("Phone number must be exactly 10 digits.")
        return number

class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    category = db.Column(db.String)

    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError("Content must be at least 250 characters in length.")
        return content

    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError("Summary must be less than 250 characters in length.")
        return summary

    @validates('category')
    def validate_category(self, key, category):
        if category not in ['Fiction', 'Non-Fiction']:
            raise ValueError("Category must be 'Fiction' or 'Non-Fiction'.")
        return category

    @validates('title')
    def validate_title(self, key, title):
        clickbait_list = ["Won't Believe", "Secret", "Top", "Guess"]
        for clickbait in clickbait_list:
            if clickbait in title:
                return title
        raise ValueError("Title does not contain sufficient clickbait.")
