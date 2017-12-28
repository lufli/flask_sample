from StringIO import StringIO
import unittest
from app import app

class AppTestCase(unittest.TestCase):
    # If I make some changes
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
    def test_upload(self):
        f = open('./Flask.jpg', 'r')
        data = StringIO(f.read())
        res = self.client.post(
            '/img',
            content_type='multipart/form-data',
            data={'file': (data, 'Flask.jpg')},
            follow_redirects=True)
        f.close()
        f = open('./Flask.jpg', 'r')
        assert res.data == f.read()
        f.close()
if __name__ == '__main__':
    unittest.main()