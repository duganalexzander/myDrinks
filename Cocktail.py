#Cocktail.py

class Cocktail(object):
	"""An object representing a Cocktail. Has a name, location (a page
	reference and corresponding bar book), list of ingredients,
	'%'abv, list of required barware, and a list of required glassware.
	"""

	def __init__(self, name='Name', loc=("Book", 0), ingr=[], strength=0.0,
		barware=[], glassware=[]):
		"""Creates a Cocktail. Default values will, hopefully, prevent code from
		crashing but will not contain any true/useful information.
		"""

		self.name = name
		self.loc  = loc
		self.ingr = ingr
		self.strength = strength
		self.barware = barware
		self.glassware = glassware
		
	def __str__(self):
		s=''
		s=s+self.name
		s=s+'\nBook: %s\nPage: %d\nIngredients:\n' % (self.loc[0], self.loc[1])
		for ingredient in self.ingr:
			s=s+'%s \n' % (ingredient)
		return s

	def get_name(self):
		"""Returns the name of the cocktail"""
		return self.name

	def get_loc(self):
		"""Returns the location (Book,Page) of the cocktail as a 2-tuple"""
		return self.loc

	def get_ingr(self):
		"""Returns the list of ingredients"""
		return self.ingr

	def get_str(self):
		"""Returns the '%'abv as a float"""
		return self.strength


class Ingredient(object):
	"""An object representing an ingredient in a cocktail, such as a lime or liquor. 
	"""

	def __init__(self, name='Name', replace=[]):
		"""Creates an ingredient."""
		self.name = name
		self.replace = replace

	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def set_replace(self, replacelist):
		self.replace = replacelist

	def get_replace(self):
		return self.replace
