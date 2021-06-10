import unittest
import requests
import Constants

class TestSiteOnline(unittest.TestCase):
    def test_site_active(self):
        response=requests.get(Constants.BASE_URL,timeout=10)
        self.assertEqual(response.status_code,200)


if __name__=="__main__":
    unittest.main()