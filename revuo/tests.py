from django.test import LiveServerTestCase, TestCase
from selenium import webdriver


class PortalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.quit()


    def test_home_page(self):
        """
        home page test at /
        """
        self.browser.get(self.live_server_url + '/')
        self.assertIn('Home', self.browser.title)
