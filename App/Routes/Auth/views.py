from flask import render_template, Blueprint, request, flash, url_for, redirect, jsonify, make_response, session

auth = Blueprint('auth', __name__)