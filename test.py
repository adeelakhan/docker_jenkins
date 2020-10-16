import unittest
from app import app
class TestHello(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')
    def test_adeel(self):
        rv = self.app.get('/adeel')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b"Adeel's Page!\n")
if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
