from aiohttp import web
import asyncio


async def hello(request):
    await asyncio.sleep(2)
    return web.Response(text="Hello Lays")

app = web.Application()
app.router.add_get('/', hello)

if __name__ == "__main__":
    web.run_app(app)
