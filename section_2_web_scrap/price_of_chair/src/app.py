import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/lg-oled55b8slc-oled-hdr-4k-ultra-hd-smart-tv-55-inch-with-freeview-play-freesat-hd-dolby-atmos-picture-on-metal-design-crescent-stand-ultra-hd-certified-black-silver/p3661161")
content = request.content
#
#<meta itemprop="price" content="89.00">

soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class":"price price--large"})
#print(element.text.strip())

string_price = element.text.strip() #£1,289.00

#now we want to remove the £ sign and convert to float
price_without_symbol = string_price[1:].replace(',', '')
#print boolean
#print(float(price_without_symbol) < 200)
price = float(price_without_symbol)

if price < 1000:
    print("You should buy the tv")
    print("The current price is {}".format(string_price))
else:
    print("Don't buy the TV yet.")
    print("The current price is {}".format(string_price))
