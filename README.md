# GroceryStoreDroneDelivery
Use drones to deliver groceries from our grocery store

To connect with MYSQL

Run this command 
pip install pymysql
Add these line to manage.py
import pymysql 
pymysql.install_as_MySQLdb()

Add these line to setting.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grocery_store',
        'USER': 'root',
        'PASSWORD': 'anypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


