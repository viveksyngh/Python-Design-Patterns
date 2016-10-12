from abc import ABCMeta, abstractmethod


class Section:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def describe(self):
		pass


class PersonalSection(Section):

	def describe(self):
		print "Personal Section"


class AlbumSection(Section):

	def describe(self):
		print "Album Section"


class PatentSection(Section):

	def describe(self):
		print "Patent Section"


class PublicationSection(Section):

	def describe(self):
		print "Publication Section"


class Profile:
	__metaclass__ = ABCMeta

	def __init__(self):
		self.sections = []
		self.create_profile()
	
	@abstractmethod
	def create_profile(self):
		pass

	def get_section(self):
		return self.sections

	def add_section(self, section):
		self.sections.append(section)


class Linkedin(Profile):

	def create_profile(self):
		self.add_section(PersonalSection())
		self.add_section(PatentSection())
		self.add_section(PublicationSection())


class Facebook(Profile):

	def create_profile(self):
		self.add_section(PersonalSection())
		self.add_section(AlbumSection())


if __name__ == '__main__':
	profile_type = 'Facebook'
	profile = eval(profile_type)()
	print "Profile type: ", type(profile).__name__
	# Profile type:  Facebook
	print profile.get_section()
	# [<__main__.PersonalSection object at 0x7f6fda5b4590>, <__main__.AlbumSection object at 0x7f6fda5b45d0>]

