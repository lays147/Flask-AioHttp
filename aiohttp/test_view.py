from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from main import app


class TestViewGet(AioHTTPTestCase):

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        return app

    @unittest_run_loop
    async def test_view(self):
        request = await self.client.get('/')
        assert request.status == 200
        text = await request.text()
        assert "Hello Lays" == text
