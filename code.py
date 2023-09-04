import requests

import matplotlib.pyplot as plt

try:
    url_1 = "https://api.nobitex.ir/v2/orderbook/BTCIRT"
    url_2 = "https://api.nobitex.ir/v2/orderbook/ETHIRT"
    url_3 = "https://api.nobitex.ir/v2/orderbook/SHIBIRT"
    url_4 = "https://api.nobitex.ir/v2/orderbook/MANAIRT"
    url_5 = "https://api.nobitex.ir/v2/orderbook/DOGEIRT"
    url_6 = "https://api.nobitex.ir/v2/orderbook/XRPIRT"
    url_7 = "https://api.nobitex.ir/v2/orderbook/ADAIRT"
    url_8 = "https://api.nobitex.ir/v2/orderbook/AAVEIRT"
    url_9 = "https://api.nobitex.ir/v2/orderbook/BNBIRT"
    url_10 = "https://api.nobitex.ir/v2/orderbook/LTCIRT"
    url_11 = "https://api.nobitex.ir/v2/orderbook/BCHIRT"

    btc = requests.get(url_1).json()
    eth = requests.get(url_2).json()
    shib = requests.get(url_3).json()
    mana = requests.get(url_4).json()
    doge = requests.get(url_5).json()
    ripl = requests.get(url_6).json()
    ada = requests.get(url_7).json()
    aave = requests.get(url_8).json()
    bnb = requests.get(url_9).json()
    ltc = requests.get(url_10).json()
    #bch = requests.get(url_11).json()
    x= [btc , eth , shib , mana , doge, ripl, ada ,aave, bnb, ltc,]
    

    arz = ['BTC',"ETH","SHIB","MANA","DOGE","Ripl", "carnado","AAVE",'BNB',"LTC",]
    price = []

    for i in x:
        price.append(int(i["lastTradePrice"])/10000000)
        # btc = 10000000

    plt.plot(arz,price,
            label='price for the curency ',marker='o',ms=2,mfc='r',linewidth=0.8)

    
    plt.ylabel('Price(Million Toman)')
    plt.legend()
    plt.show()

except:
    print("   No Internet  ")



