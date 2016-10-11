# Metaclasses and Singleton

class MyInt(type):

	def __call__(cls, *args, **kwargs):
		print "Here is MyInt ", args
		print "Do whatever you want to do with these objects."
		return type.__call__(cls, *args, **kwargs)



class int:
	__metaclass__ = MyInt
	def __init__(self, x, y):
		self.x = x
		self.y = y


i = int(4, 5)


# Singleton implementaion with Metaclass

class MetaSingleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = type.__call__(cls, *args, **kwargs)
		return cls._instances[cls]

class Singleton:
	__metaclass__ = MetaSingleton


s1 = Singleton()
s2 = Singleton()

print "s1 ", s1 # s1  <__main__.Singleton object at 0x7f783d273410>
print "s2 ", s2 # s2  <__main__.Singleton object at 0x7f783d273410>





