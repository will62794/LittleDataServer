from DataSource import *

class Stocks(DataSource):
	"""pulls Stock info from the Web"""
	def __init__(self):
		super(StockBroker, self).__init__()
		self.auth_token="dsahFHUiewjjd"
		
	def getAllStockCompanies(self):
		#data=Quandl.get('PRAGUESE/PX',authtoken=self.auth_token)
		pass
		#return data.head()
		
