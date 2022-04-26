from email.mime import application
from App import create_app

application = create_app('default')

if __name__ =='__main__':
	application.run(host="0.0.0.0", port=3100)