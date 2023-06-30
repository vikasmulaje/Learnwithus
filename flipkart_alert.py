import requests
from bs4 import BeautifulSoup
import time
  
product_url = "https://www.flipkart.com/samsung-t7-1-tb-external-solid-state-drive-ssd/p/itmce3d59cd47952?pid=ACCFTZGREYWPY4GE&lid=LSTACCFTZGREYWPY4GEO8YLTB&marketplace=FLIPKART&q=ssd+samsung+&store=6bo%2Fjdy%2Fdus&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=0e2d4260-4ff3-4857-bc8b-0b62e628f00d.ACCFTZGREYWPY4GE.SEARCH&ppt=sp&ppn=sp&qH=e941ee0cc20e8ed9"
  
target_price = 8000
  
  
def check_price():
    # fetch webpage
    r = requests.get(product_url)
    # parse the html
    soup = BeautifulSoup(r.content, 'html5lib')
    # extract price using class '_16Jk6d'
    price = soup.find('div', attrs={"class": "_16Jk6d"}).text
    # remove Rs symbol from price
    price_without_Rs = price[1:]
    # remove commas from price
    price_without_comma = price_without_Rs.replace(",", "")
    # convert price from string to int
    int_price = int(price_without_comma)
    return int_price
  
  
cur_price = check_price()
print(f"Current price is {cur_price}")
print("We will inform you, once price of product hits out target price")
print("Waiting...")
while True:
    # get current price
    cur_price = check_price()
    if cur_price <= target_price:
        print(f"Its time to buy product, its current price is {cur_price}")
        break
    # wait for 1 minute to check again
    time.sleep(60)