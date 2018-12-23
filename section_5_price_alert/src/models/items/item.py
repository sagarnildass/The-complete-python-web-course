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
        tag_name = store.tag_name
        query = store.query
        self.price = self.load_price(tag_name, query)
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Item {} with url {}>".format(self.name, self.url)

    def load_price(self, tag_name, query):
        #Amazon: <span id="priceblock_ourprice" class="a-size-medium a-color-price">$2,447.99</span>
        request = requests.get(self.url)
        content = request.content
        #
        #<meta itemprop="price" content="89.00">

        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(tag_name, query)
        #print(element.text.strip())

        string_price = element.text.strip() #£1,289.00

        pattern = re.compile("(\d+.\d+)")
        match = pattern.search(string_price)

        return match.group()

    def save_to_mongo(self):
        Database.insert(ItemConstants.COLLECTION, self.json())

    def json(self):
        return {
        "name":self.name,
        "url":self.url,
        "_id":self._id
        }
