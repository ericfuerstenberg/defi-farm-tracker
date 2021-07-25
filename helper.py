from pycoingecko import CoinGeckoAPI

class Util():
    def getPrice(token):
        
        cg = CoinGeckoAPI()
        data = cg.get_price(ids=token, vs_currencies='usd')
        price = data[token]['usd']

        return price