import pymongo
import components.base
import importlib
import esper

from components.player import *

client = pymongo.MongoClient()
db = client.mmo_db

def save_player(entity, world):
	components = world.components_for_entity(entity)
	result = {'components':[]}
	for c in components:
		result.update(c.serialize())
		result['components'].append(type(c).__name__)

	db = client.mmo_db
	player = db.players.update({'email':result['email']}, result, True)
	print(player)


def load_player(email, world):
	db = client.mmo_db
	data = db.players.find_one({'email':email})
	if data:
		player = world.create_entity()
		for c in data['components']:
			ComponentClass = getattr(components.base, c)
			world.add_component(player, ComponentClass(**data))
		return player
	return None

if __name__ == '__main__':
	world = esper.World()
	player = world.create_entity()
	world.add_component(player, Level(4))
	world.add_component(player, Title("Blacksmith"))
	world.add_component(player, Health(120, 60, 1.2))
	world.add_component(player, Account('test@example.com', 'password'))

	id = save_player(player, world)

	loaded_player = load_player('test@example.com', world)

	import pdb;pdb.set_trace()






