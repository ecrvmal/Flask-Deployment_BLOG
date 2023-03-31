import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command('init-db')
def init_db():
    from wsgi import app

    # import models for creating tables
    from blog.models import User

    db.create_all(app=app)


@click.command('create-users')
def create_init_user():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='user1@mail.ru', password=generate_password_hash('123'))
        )
        db.session.add(
            User(email='user2@mail.ru', password=generate_password_hash('123'))
        )
        db.session.add(
            User(email='user3@mail.ru', password=generate_password_hash('123'))
        )
        db.session.add(
            User(email='user4@mail.ru', password=generate_password_hash('123'))
        )
        db.session.add(
            User(email='user5@mail.ru', password=generate_password_hash('123'))
        )
        db.session.commit()
