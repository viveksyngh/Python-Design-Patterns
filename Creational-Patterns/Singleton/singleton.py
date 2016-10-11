# Classical implementation of singleton in python

class Singleton(object):
	
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance

first_object = Singleton()
print first_object, id(first_object) 
# <__main__.Singleton object at 0x7fe41d484150> 140617720545616

second_object = Singleton()
print second_object, id(second_object)
# <__main__.Singleton object at 0x7fe41d484150> 140617720545616


# Lazy instansiation in singleton patterns
class LazySingleton(object):
	__instance = None

	def __init__(self):
		if not LazySingleton.__instance:
			print "__init__ method was called."
		else:
			print "Instance already created ", self.getInstance()

	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance = LazySingleton()
		return cls.__instance

s = LazySingleton()
print LazySingleton.getInstance() # Objects gets created here
s1 = LazySingleton() # Object already created


# Singleton real world examples

# Database connection
import sqlite3

class MetaSingleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = type.__call__(cls, *args, **kwargs)
		return cls._instances[cls]


class Database(object):
	__metaclass__ = MetaSingleton
	connection = None

	def connect(self):
		if self.connection is None:
			self.connection = sqlite3.connect("db.sqlite3")
			self.cursorobj = self.connection.cursor()
		return self.cursorobj

conn1 = Database().connect()
conn2 = Database().connect()

print "Connection 1 ", conn1 # Connection 1  <sqlite3.Cursor object at 0x7f6ce1450dc0>
print "Connection 2 ", conn2 # Connection 2  <sqlite3.Cursor object at 0x7f6ce1450dc0>


# Server Health check examples

class HealthCheck(object):
	__instance = None

	def __new__(cls, *args, **kwargs):
		if not HealthCheck.__instance:
			HealthCheck.__instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
		return HealthCheck.__instance

	def __init__(self):
		self._servers = []

	def add_server(self):
		self._servers.append("Server 1")
		self._servers.append("Server 2")
		self._servers.append("Server 3")
		self._servers.append("Server 4")

	def change_server(self):
		self._servers.pop()
		self._servers.append("Server 5")

	def get_servers(self):
		return self._servers


hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.add_server()

print hc1.get_servers() # ['Server 1', 'Server 2', 'Server 3', 'Server 4']
print hc2.get_servers() # ['Server 1', 'Server 2', 'Server 3', 'Server 4']

hc2.change_server()

print hc1.get_servers() # ['Server 1', 'Server 2', 'Server 3', 'Server 5']
print hc2.get_servers() # ['Server 1', 'Server 2', 'Server 3', 'Server 5']
