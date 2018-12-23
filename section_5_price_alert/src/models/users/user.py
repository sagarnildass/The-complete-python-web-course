import uuid
from common.database import Database
from common.utils import Utils
import models.users.errors as UserErrors

class User(object):

    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        #This method verifies that the email/password combo sent by the site forms is valid or not
        #param email: user's email
        #parma password: a sha512 hashed password
        user_data = Database.find_one("users", {"email":email})  #password in pbkdf2_sha512 (hashed twice)
        if user_data is None:
            #tell the user that thei email does not exist
            raise UserErrors.UserNotExistsError("Your user does not exist!")
        if not Utils.check_hashed_password(password, user_data['password']):
            #tell the user that their password is wrong
            raise UserErrors.IncorrectPasswordError("Your password is incorrect")

        return True

    @staticmethod
    def register_user(email, password):
        #This method registers a user using email and password. The password already comes as hashed sha512
        #param email: user's email
        #param password: sha-512 hashed password
        #returns True if registered successfully, and False otherwise(exceptions can also be raised)
        user_data = Database.find_one("users", {"email":email})

        if user_data is not None:
            #Tell user they are already registered
            pass

        if not Utils.email_is_valid(email):
            #Tell the user that their email is not constructed properly
            pass

        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {
        "_id":self._id,
        "email":self.email,
        "password":self.password
        }
