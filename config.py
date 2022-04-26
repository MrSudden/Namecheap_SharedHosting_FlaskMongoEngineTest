class Config:
    SECRET_KEY = 'UlcJ>fg0TPN-2188dCid<$i$'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """docstring for DevelopmentConfig"""
    SECRET_KEY = 'UlcJ>fg0TPN-2188dCid<$i$'
    DEBUG=True
    THREADED=True

    TEMPLATES_AUTO_RELOAD=True
    EXPLAIN_TEMPLATE_LOADING=False
    JSON_SORT_KEYS=True
    JSONIFY_PRETTYPRINT_REGULAR=True
    UPLOAD_FOLDER = ''
    MAIL_SERVER=''
    MAIL_USERNAME=''
    MAIL_PASSWORD=''
    MAIL_DEFAULT_SENDER =''
    MAIL_PORT=587
    MAIL_USE_SSL=False
    MAIL_USE_TLS=True
    
    # MongoEngine config
    MONGODB_SETTINGS = {
        'db': 'template',
        'host': 'localhost',
        'port': 27017
    }

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

# /usr/lib/postgresql/10/bin/pg_ctl -D /var/lib/postgresql/10/main -l logfile start
# sudo -i -u postgres