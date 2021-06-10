import unittest
import requests
import Constants

class TestSiteOnline(unittest.TestCase):
    def test_site(self):
        response=requests.get(Constants.BASE_URL)
        self.assertEqual(response.status_code,200)


if __name__=="__main__":
    unittest.main()