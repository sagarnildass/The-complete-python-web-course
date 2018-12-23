from passlib.hash import pbkdf2_sha512
import re

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password):
        #hashes a password using pbkdf2_sha512
        #param password: The sha512 password from login or register form
        #returns a pbkdf2_sha512 encrypted password
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        #check that the password the user sent matches with the database
        #The database password is encrypted
        #param password: sha512 hashed password
        #param hashed_password:pbkdf2_sha512 encrypted password
        #returns True is passwords match and False otherwise
        return pbkdf2_sha512.verify(password, hashed_password)
