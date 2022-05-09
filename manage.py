from email.mime import application
from App import create_app

app = create_app('default')
application = app

if __name__ =='__main__':
	app.run(host="0.0.0.0", port=3100)