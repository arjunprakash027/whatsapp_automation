import pywhatkit
from datetime import date
import json
import time

today = date.today()
f = open('stocks_info')
data = json.load(f)
print(data)
stock_list = ["TATACONSUM","BERGEPAINT","COALINDIA"]
for i in range(len(stock_list)):
    name = data['Stock_details'][str(i)]['Name']
    price = data['Stock_details'][str(i)]['price']
    fifty_ma = data['Stock_details'][str(i)]['50 days ma']
    twohundred_ma = data['Stock_details'][str(i)]['200 days ma']
    pywhatkit.sendwhats_image("FbFceNKFlX7L7FFNgy9ywN", "{}.png".format(stock_list[i]),"Name:{}\nprice:{}\n50DaysMA:{}\n200DaysMA:{}".format(name,price,fifty_ma,twohundred_ma))
    time.sleep(3)