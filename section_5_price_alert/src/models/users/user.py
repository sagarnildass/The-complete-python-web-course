import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors

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
