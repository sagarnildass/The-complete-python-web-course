from bs4 import BeautifulSoup
import requests
import re
from common.database import Database
import models.items.constants as ItemConstants
from models.stores.store import Store
import uuid

class Item(object):

    def __init__(self, name, url, _id=None):
        self.name = name
        self.url = url
        store = Store.find_by_url(url)
        self.tag_name = store.tag_name
        self.query = store.query
        self.price = None
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Item {} with url {}>".format(self.name, self.url)

    def load_price(self):
        #Amazon: <span id="priceblock_ourprice" class="a-size-medium a-color-price">$2,447.99</span>
        request = requests.get(self.url)
        content = request.content
        #
        #<meta itemprop="price" content="89.00">

        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        #print(element.text.strip())

        string_price = element.text.strip() #£1,289.00

        pattern = re.compile("(\d+.\d+)")
        match = pattern.search(string_price)
        self.price = float(match.group())
        return self.price

    def save_to_mongo(self):
        Database.insert(ItemConstants.COLLECTION, self.json())

    def json(self):
        return {
        "name":self.name,
        "url":self.url,
        "_id":self._id
        }

    @classmethod
    def get_by_id(cls, item_id):
        return cls(**Database.find_one(ItemConstants.COLLECTION, {"_id":item_id}))
