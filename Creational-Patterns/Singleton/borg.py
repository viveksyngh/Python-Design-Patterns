# Borg or Monostate design pattern, All objects shares same state

# Method 1

class Borg(object):

	__shared_state = {"a": "1"}
	
	def __init__(self):
		self.x = 1
		print self.__dict__
		self.__dict__ = self.__shared_state
		print self.__dict__


b = Borg()

b1 = Borg()

b.x = 4

print "First borg object ", b 
# First borg object  <__main__.Borg object at 0x7fa7091c1150>

print "Second borg object ", b1 
# Second borg object  <__main__.Borg object at 0x7fa7091c1190> 

print "First borg object state ", b.__dict__ 
# First borg object state  {'a': '1', 'x': 4}

print "Second borg object states ", b1.__dict__ 
# Second borg object states  {'a': '1', 'x': 4}


# Method 2

class Borg(object):

	__shared_state = {}

	def __new__(cls, *args, **kwargs):
		obj = super(Borg, cls).__new__(cls, *args, **kwargs)
		obj.__dict__ = cls.__shared_state
		return obj

b = Borg()

b1 = Borg()

b.x = 4

print "First borg object ", b 
# First borg object  <__main__.Borg object at 0x7f5124398390>

print "Second borg object ", b1 
# Second borg object  <__main__.Borg object at 0x7f5124398250>

print "First borg object state ", b.__dict__ 
# First borg object state  {'x': 4}

print "Second borg object states ", b1.__dict__ 
# Second borg object states  {'x': 4}
