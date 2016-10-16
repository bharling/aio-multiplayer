from aiohttp import web
from aiohttp_utils import Response, negotiation, run, path_norm
import pathlib
import jinja2
import aiohttp_jinja2
import sockjs
import logging
from server.game import Game



class GameApplication(web.Application):
    def __init__(self, *args, **kwargs):
        super(GameApplication, self).__init__(*args, **kwargs)
        negotiation.setup(self)
        aiohttp_jinja2.setup(self,
            loader=jinja2.FileSystemLoader('/vagrant/templates/'))
        self.setup_routes()
        path_norm.setup(self)
        self.game = Game(self)

    def setup_routes(self):
        self.router.add_route('GET', '/', self.index)
        self.router.add_static('/static/', '/vagrant/static/', name='static')
        sockjs.add_endpoint(self, self.sockjs_handler, name="game", prefix="/sockjs/")

    @aiohttp_jinja2.template('index.html')
    def index(self, request):
        return {
            'title':'Whats up ' + request.GET.get('name', 'World'),
            'app': self,
        }

    def sockjs_handler(self, msg, session):
        if msg.tp == sockjs.MSG_OPEN:
            session.manager.broadcast("Someone Joined")
            self.game.player_joined(session)

        if msg.tp == sockjs.MSG_MESSAGE:
            session.manager.broadcast(msg.data)

        if msg.tp == sockjs.MSG_CLOSED:
            session.manager.broadcast("Someone Left")

logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')
app = GameApplication(router=web.UrlDispatcher(), debug=True)
if __name__ == "__main__":
    
    run(
        app,
        app_uri='game.main:app',
        reload=True,
        port=8000,
        host='0.0.0.0'
    )
