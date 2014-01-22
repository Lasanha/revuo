from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from model_mommy import mommy
from models import Author, Admin, Item


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
        # create some news
        for i in xrange(10):
            mommy.make(Item, category='N', authorized=True)
        # then check the page
        self.browser.get(self.live_server_url + '/news')
        self.assertIn('News', self.browser.title)
        news_list = self.browser.find_element_by_name('news_list')
        news_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(news_list)
        self.assertIsNotNone(news_item)


    def test_media_page(self):
        """
        news page test at /media
        """
        # create some media
        for i in xrange(10):
            mommy.make(Item, category='V', authorized=True)
        # and check page
        self.browser.get(self.live_server_url + '/media')
        self.assertIn('Media', self.browser.title)
        video_list = self.browser.find_element_by_name('media_list')
        video_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(video_list)
        self.assertIsNotNone(video_item)


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
        # create some media
        for i in xrange(10):
            mommy.make(Item, category='B', authorized=True)
        # aaaand check page
        self.browser.get(self.live_server_url + '/blog')
        self.assertIn('Blog', self.browser.title)
        posts_list = self.browser.find_element_by_name('post_list')
        posts_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(posts_list)
        self.assertIsNotNone(posts_item)


    def test_staff_page(self):
        """
        news page test at /staff
        """
        self.browser.get(self.live_server_url + '/staff')
        self.assertIn('Staff', self.browser.title)


class BackendTest(TestCase):

    def test_author_model(self):
        """
        author model test
        """
        author = mommy.make(Author)
        self.assertTrue(isinstance(author, Author))
        self.assertEqual(
            author.__unicode__(), 
            ' '.join([author.user.first_name, author.user.last_name])
            )


    def test_admin_model(self):
        """
        admin model test
        """
        admin = mommy.make(Admin)
        self.assertTrue(isinstance(admin, Admin))
        self.assertEqual(
            admin.__unicode__(), 
            ' '.join([admin.user.first_name, admin.user.last_name])
            )


    def test_item_model(self):
        """
        item model test
        """
        item = mommy.make(Item)
        self.assertTrue(isinstance(item, Item))
        self.assertTrue(isinstance(item.author, Author))
