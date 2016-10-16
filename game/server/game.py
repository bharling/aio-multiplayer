
import esper
import time
import asyncio

FPS = 1.0/2.0

class Game(object):
    """docstring for Game"""
    def __init__(self, app):
        super(Game, self).__init__()
        self.app = app
        self.world = esper.World()
        self.players = {} # indexed by session key from sockjs
        self.processors = []
        self.running = True
        self.elapsed = 0.0
        asyncio.ensure_future(self.game_loop())

    def player_joined(self, session, email=None):
        ent = self.world.create_entity()
        ent.socket = session
        self.players[session.id] = ent

    async def game_loop(self):
        if not getattr(self, 'last_tick', None):
            self.last_tick = time.time()
        while self.running:
            current = time.time()
            dt = current - self.last_tick
            self.last_tick = current
            self.elapsed += dt
            if self.elapsed >= FPS:
                for player in self.players.values():
                    player.socket.send('Tick')
                self.elapsed = 0
            await asyncio.sleep(0)


