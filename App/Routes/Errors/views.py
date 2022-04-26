from flask import render_template, Blueprint

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error(err):
    return render_template('./errors/error.html',error =err, error_val = 404)

@errors.app_errorhandler(400)
def bad_request(err):
		return render_template("./errors/error.html", error = err, error_val = 400)

@errors.app_errorhandler(401)
def un_authenticated(err):
	return render_template("./errors/error.html", error = err, error_val = 401)

@errors.app_errorhandler(403)
def for_bidden(err):
	return render_template("./errors/error.html", error = err, error_val = 403)


@errors.app_errorhandler(405)
def four_oh_five(err):
	return render_template("./errors/error.html", error = err, error_val = 405)

@errors.app_errorhandler(406)
def not_acceptable(err):
	return render_template("./errors/error.html", error = err, error_val = 406)

@errors.app_errorhandler(500)
def error_in_service(err):
	return render_template("./errors/error.html", error = err, error_val = 500)