from .base import * # NOQA
# 上面的NO~注释告诉REP8规范检测工具，这个地方不需要检测

DEBUG = True

DATABASES = {
    'default': {
        # 连接mysql数据库
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'yong',
        'PASSWORD': 'Free7890',
        # 将要连接的数据库服务器IP和Port
        'HOST': '127.0.0.1',
        'PORT': '3306'
	# 'CONN_MAX_AGE': 5*60,
	# 'OPTIONS': {'charset': 'utf8mb4'}
    }
}