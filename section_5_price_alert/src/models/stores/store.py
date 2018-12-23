import uuid
from common.database import Database
import models.stores.constants as StoreConstants
import models.stores.errors as StoreErrors

class Store(object):

    def __init__(self, name, url_prefix, tag_name, query, _id=None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Store {}>".format(self.name)

    def json(self):
        return {
        "_id":self._id,
        "name":self.name,
        "url_prefix":self.url_prefix,
        "tag_name":self.tag_name,
        "query":self.query
        }

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"_id":id}))

    def save_to_mongo(self):
        Database.insert(StoreConstants.COLLECTION, self.json())

    @classmethod
    def get_by_name(cls, store_name):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"name":store_name}))

    @classmethod
    def get_by_url_prefix(cls, url_prefix):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"url_prefix":{"$regex":'^{}'.format(url_prefix)}}))

    @classmethod
    def find_by_url(cls, url):
        for i in range(len(url)+1, 0-1, -1):
            try:
                if Database.find_one(StoreConstants.COLLECTION, {'url_prefix': {"$regex": '^{}'.format(url[:i])}}) is not None:
                    store = cls.get_by_url_prefix(url[:i])
                    return store

            except:
                raise StoreErrors.StoreNotFoundException("The URL Prefix used to find the store did not fetch any resutls")
