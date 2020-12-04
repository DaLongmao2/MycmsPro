#encoding:utf-8



DB_USERNAME = 'root'
DB_PASSWORD = '1122'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'mycms'


# PERMANENT_SESSION_LIFETIME =

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

CMS_USER_ID = '1231'
FRONT_USER_ID = 'xxxxasfasfacxhgf'


# 邮件配置
# 服务器ip地址
MAIL_SERVER = "smtp.qq.com"
# 端口号:TLS对应587,SSL对应465
MAIL_PORT = "587"
MAIL_USE_TLS = True
# MAIL_USE_SSL : 默认为 False
# 发送者邮箱
MAIL_USERNAME = "dalongmao.zhang@qq.com"
# 发送者QQ邮箱授权码(进入邮箱发送短信申请即可，具体参照下图)
MAIL_PASSWORD = "szwwjgmdhdbybfab"
# 默认发送者
MAIL_DEFAULT_SENDER = "dalongmao.zhang@qq.com"


SECRET_KEY = '123'

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False


START = 0
PERPAGE = 10

Album_PERPAGE = 10


CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
