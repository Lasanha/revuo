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


    def test_news_page(self):
        """
        news page test at /news
        """
        self.browser.get(self.live_server_url + '/news')
        self.assertIn('News', self.browser.title)


    def test_media_page(self):
        """
        news page test at /media
        """
        self.browser.get(self.live_server_url + '/media')
        self.assertIn('Media', self.browser.title)


    def test_publications_page(self):
        """
        news page test at /publications
        """
        self.browser.get(self.live_server_url + '/publications')
        self.assertIn('Publications', self.browser.title)


    def test_blog_page(self):
        """
        news page test at /blog
        """
        self.browser.get(self.live_server_url + '/blog')
        self.assertIn('Blog', self.browser.title)


    def test_staff_page(self):
        """
        news page test at /staff
        """
        self.browser.get(self.live_server_url + '/staff')
        self.assertIn('Staff', self.browser.title)




