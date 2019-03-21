import os


#basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    ''' Secret Key Config '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    ''' SMTP Server Config '''
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    ADMINS = ['x@gmail.com']
    POSTS_PER_PAGE = 25
