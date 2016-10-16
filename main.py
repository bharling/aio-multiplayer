from aiohttp import web

from aiohttp_utils import Response, routing, negotiation, run, path_norm


app = web.Application(router=routing.ResourceRouter())


async def index(request):
    return Response('Hi There')

class HelloResource():
    async def get(self, request):
        name = request.GET.get('name', 'World')
        return response({
            'message': 'Hello' + name
        })

with routing.add_route_context(app) as route:
    route('GET', '/', index)

# app.router.add_resource_object('/', HelloResource())

# Content negotiation
# negotiation.setup(
#     app, renderers={
#         'application/json': negotiation.render_json
#     }
# )

path_norm.setup(app)

if __name__ == '__main__':
    # Development server
    run(
        app,
        # app_uri='main:app',
        # reload=True,
        port=8000,
        host='0.0.0.0'
    )
        