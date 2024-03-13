import json
from aiohttp import web
from main import Analytics

analytics = Analytics()


async def handle(request):
    return web.Response(
        text=json.dumps(await analytics.data(), indent=4),
        content_type="application/json",
    )


def server():
    app = web.Application()
    app.router.add_get("/", handle)

    web.run_app(app, host="localhost", port=8081)


if __name__ == "__main__":
    server()
