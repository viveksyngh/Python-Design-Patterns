from abc import ABCMeta, abstractmethod

class PizzaFactory:

	__metaclass__ = ABCMeta

	@abstractmethod
	def create_veg_pizza(self):
		pass

	@abstractmethod
	def create_non_veg_pizza(self):
		pass


class IndianPizzaFactory(PizzaFactory):

	def create_veg_pizza(self):
		return DeluxeVeggiePizza()

	def create_non_veg_pizza(self):
		return ChickenPizza()


class USPizzaFactory(PizzaFactory):

	def create_veg_pizza(self):
		return MexicanVegPizza()

	def create_non_veg_pizza(self):
		return HamPizza()


class VegPizza:
	
	__metaclass__ = ABCMeta

	@abstractmethod
	def prepare(self):
		pass


class NonVegPizza:
	
	__metaclass__ = ABCMeta

	@abstractmethod
	def serve(self, VegPizza):
		pass


class DeluxeVeggiePizza(VegPizza):
	
	def prepare(self):
		print "Prepare ", type(self).__name__


class ChickenPizza(NonVegPizza):

	def serve(self, VegPizza):
		print type(self).__name__, "is served with Chicken on", type(VegPizza).__name__


class MexicanVegPizza(VegPizza):
	
	def prepare(self):
		print "Prepare ", type(self).__name__


class HamPizza(NonVegPizza):

	def serve(self, VegPizza):
		print type(self).__name__, "is served with Ham on", type(VegPizza).__name__


class PizzaStore:

	def __init__(self):
		pass

	def makePizzas(self):
		for factory in [IndianPizzaFactory(), USPizzaFactory()]:
			self.factory = factory
			self.NonVegPizza = self.factory.create_non_veg_pizza()
			self.VegPizza = self.factory.create_veg_pizza()
			self.VegPizza.prepare()
			self.NonVegPizza.serve(self.VegPizza)

pizza = PizzaStore()
pizza.makePizzas()

# Prepare  DeluxeVeggiePizza
# ChickenPizza is served with Chicken on DeluxeVeggiePizza
# Prepare  MexicanVegPizza
# HamPizza is served with Ham on MexicanVegPizza