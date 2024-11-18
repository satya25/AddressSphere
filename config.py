import os
 
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'a15c52ce500a9693cc2ee0619c8aed25')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://root:@localhost/address_sphere')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
