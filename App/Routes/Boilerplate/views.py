from email.policy import default
from tokenize import String
from flask import Flask, Blueprint, render_template, url_for, jsonify, request, redirect
from json import loads, dumps
from App import db
from Model import *

boiler = Blueprint('boiler', __name__)

@boiler.route('/')
def main():
    # return render_template('index.html')
    user1 = User(fullname="Abdul Alhass")
    user1.tags = ["db", "section"]
    user1.save()
    users = User.objects()
    # users.delete()
    # return jsonify([str(user.id) for user in users])
    return jsonify(users)