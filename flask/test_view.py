from main import app
import unittest


class TestViewGet(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_view(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, b"Hello Lays")


if __name__ == '__main__':
    unittest.main()
