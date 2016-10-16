import esper

class Component(object):
	"""Base class for components, just provides serialization
	and that's it."""

	def serialize(self):
		result = self.__dict__
		# result = {type(self).__name__:self.__dict__}
		return result




# if __name__ == '__main__':
# 	world = esper.World()

# 	player = world.create_entity()
# 	world.add_component(player, Level(4))
# 	world.add_component(player, Title("Blacksmith"))
# 	world.add_component(player, Health(120, 60, 1.2))
# 	world.add_component(player, Account('test@example.com', 'password'))

# 	components = world.components_for_entity(player)
# 	result = {'components':[]}
# 	for c in components:
# 		result.update(c.serialize())
# 		result['components'].append(type(c).__name__)

# 	import json
# 	print(json.dumps(result, indent=4))

# 	from pymongo import MongoClient
# 	from pymongo import TEXT
# 	client = MongoClient()

# 	db = client.mmo_db
	

# 	# db.players.create_index([("email", TEXT)], unique=True)

# 	player_id = db.players.update({'email':result['email']}, result, True)
# 	print(player_id)

# 	player = db.players.find_one({'email':'test@example.com'})
# 	print(player)

# 	print(db.players.count())

# 	print(db.players.find({}))







	
		
		

		
		
