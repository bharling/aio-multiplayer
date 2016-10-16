from .base import Component

class Level(Component):
	def __init__(self, level=1, **kwargs):
		self.level = level

class Title(Component):
	def __init__(self, title="", **kwargs):
		self.title = title

class Name(Component):
	def __init__(self, name="", **kwargs):
		super(Name, self).__init__()
		self.name = name

class Health(Component):
	"""docstring for Health"""
	def __init__(self, health_max=100, health=100, heath_regen=0.5, **kwargs):
		super(Health, self).__init__()
		self.health_max = health_max
		self.health = health
		self.heath_regen = heath_regen

class Stamina(Component):
	def __init__(self, stamina_max = 100, stamina = 100, stamina_regen=0.5, **kwargs):
		self.stamina_regen = stamina_regen
		self.stamina = stamina
		self.stamina_max = stamina_max
		
class Position(Component):
	"""docstring for Position"""
	def __init__(self, x=0.0, y=0.0, z=0.0, **kwargs):
		super(Position, self).__init__()
		self.x = x
		self.y = y
		self.z = z
		
class Path(Component):
	"""docstring for Path"""
	def __init__(self, waypoints=[], **kwargs):
		super(Path, self).__init__()
		self.waypoints = waypoints

class Account(Component):
	def __init__(self, email="", password="", **kwargs):
		self.email = email
		self.password = password

