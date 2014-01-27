class NotEnoughProduct(Exception):
	"""docstring for NotEnoughProduct"""
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return self.value
class ProductOffline(Exception):
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return self.value
class ProductUnbought(Exception):
	"""docstring for ProductUnbought"""
	def __init__(self,value):
		super(ProductUnbought, self).__init__()
		self.value = value
	def __str__(self):
		return self.value
		
