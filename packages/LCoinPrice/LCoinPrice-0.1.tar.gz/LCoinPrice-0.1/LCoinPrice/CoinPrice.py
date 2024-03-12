from pycoingecko import CoinGeckoAPI

class COIN():
	def __init__(self, coin, currency):
		if coin == "ton":
			self.coin = "the-open-network"
		else:
			self.coin = coin
		self.currency = currency
	def GET(self):
		cg = CoinGeckoAPI()
		result = cg.get_price(ids=self.coin, vs_currencies=self.currency)
		return result[self.coin][self.currency]

def VALUES():
	d = {"coins": ["ton", "bitcoin"], "currency": ["usd", "rub", "uah"]}
	print(d)