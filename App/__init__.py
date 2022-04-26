from flask import Flask
from flask_mongoengine import MongoEngine
from datetime import timedelta
from flask_wtf.csrf import CSRFProtect
from os.path import join , getmtime
from os import getcwd
from config import config

db = MongoEngine()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	app.config['REMEMBER_COOKIE_DURATION'] = timedelta(minutes=5)
	csrf = CSRFProtect()
	csrf.init_app(app)
	db.init_app(app)

	@app.template_filter('autoversion')
	def autoversion_filter(filename):
		# determining fullpath might be project specific
		fullpath = join(filename)
		cwd = getcwd()
		fullpath = cwd + '/App' + fullpath
		try:
			tm = str(int(getmtime(fullpath)))
		except OSError:
			return filename
		newfilename = "{0}?v={1}".format(filename, tm)
		return newfilename

    ## Use the line below to define "BlueprintObject" from it's respective "Module"
	# from App.Routes.Module.views import BlueprintObject
	from App.Routes.Boilerplate.views import boiler

    ## Using the line format below, register BlueprintObject
	# app.register_blueprint(BlueprintObject)
	app.register_blueprint(boiler)

	## Using the line format below for csrf exemption of AnyBlueprintObject
	# csrf.exempt(AnyBlueprintObject)

	return app
