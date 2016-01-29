import asyncio
import importlib
from aiohttp.web import Application, Response
import python_hot_swap.ping as p

async def handle(request):
    importlib.reload(p)
    return Response(text=p.ping())

async def init(loop):
    app = Application(loop=loop)
    app.router.add_route('GET', '/', handle)

    srv = await loop.create_server(app.make_handler(),
                                   '127.0.0.1', 1337)
    print('Server started at http://127.0.0.1:1337')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
