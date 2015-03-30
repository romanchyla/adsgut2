# -*- coding: utf-8 -*-
"""
    adsgut.models
    ~~~~~~~~~~~~~~~~~~~~~

    Models for the users/libraries/items/tags of ADSGUT
"""
from flask_security import UserMixin, RoleMixin
from flask_sqlalchemy import SQLAlchemy as FlaskSQLAlchemy
from sqlalchemy.orm import synonym
from flask_security.utils import encrypt_password, verify_password

db = FlaskSQLAlchemy()

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))




class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    registered_at = db.Column(db.DateTime())

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class Role(RoleMixin, db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __eq__(self, other):
        return (self.name == other or
                self.name == getattr(other, 'name', None))

    def __ne__(self, other):
        return (self.name != other and
                self.name != getattr(other, 'name', None))

