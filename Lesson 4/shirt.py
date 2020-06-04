class Shirt:
	def __init__(self, shirt_color,shirt_size, shirt_style, shirt_price):
		self.color = shirt_color
		self.size = shirt_size
		self.price = shirt_price


	def change_price(self,new_price):
		self.price = new_price

	def discount(self,discout):
		return self.price * (1 - discout)

		