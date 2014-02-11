from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from model_mommy import mommy
from models import Author, Admin, NewsItem, BlogItem, VideoItem, Publication
from django.contrib.auth.models import User


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
            mommy.make(NewsItem, authorized=True)
        # then check the page
        self.browser.get(self.live_server_url + '/news')
        self.assertIn('News', self.browser.title)
        news_list = self.browser.find_element_by_name('news_list')
        news_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(news_list)
        self.assertIsNotNone(news_item)
        # news view
        news = mommy.make(NewsItem, authorized=True)
        self.browser.get(self.live_server_url + '/N/' + str(news.id))
        self.assertIn(news.title, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(news.description, body.text)
        self.assertIn(news.text, body.text)


    def test_media_page(self):
        """
        news page test at /media
        """
        # create some media
        for i in xrange(10):
            mommy.make(VideoItem, authorized=True)
        # and check page
        self.browser.get(self.live_server_url + '/media')
        self.assertIn('Media', self.browser.title)
        video_list = self.browser.find_element_by_name('media_list')
        video_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(video_list)
        self.assertIsNotNone(video_item)
        # media view
        media = mommy.make(VideoItem, authorized=True)
        self.browser.get(self.live_server_url + '/V/' + str(media.id))
        self.assertIn(media.title, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(media.text, body.text)


    def test_publications_page(self):
        """
        news page test at /publications
        """
        # create publications
        for i in xrange(10):
            mommy.make(Publication, authorized=True)
        # check page
        self.browser.get(self.live_server_url + '/publications')
        self.assertIn('Publications', self.browser.title)
        pubs_list = self.browser.find_element_by_name('pubs_list')
        pubs_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(pubs_list)
        self.assertIsNotNone(pubs_item)


    def test_blog_page(self):
        """
        news page test at /blog
        """
        # create some media
        for i in xrange(10):
            mommy.make(BlogItem, authorized=True)
        # aaaand check page
        self.browser.get(self.live_server_url + '/blog')
        self.assertIn('Blog', self.browser.title)
        posts_list = self.browser.find_element_by_name('post_list')
        posts_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(posts_list)
        self.assertIsNotNone(posts_item)
        # post view
        post = mommy.make(BlogItem, authorized=True)
        self.browser.get(self.live_server_url + '/B/' + str(post.id))
        self.assertIn(post.title, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(post.description, body.text)
        self.assertIn(post.text, body.text)


    def test_staff_page(self):
        """
        news page test at /staff
        """
        # create some users
        for i in xrange(10):
            mommy.make(Author)
        # aaaand check page
        self.browser.get(self.live_server_url + '/staff')
        self.assertIn('Staff', self.browser.title)
        authors_list = self.browser.find_element_by_name('authors_list')
        authors_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(authors_list)
        self.assertIsNotNone(authors_item)
        # post view
        user = mommy.make(User, first_name='John')
        author = mommy.make(Author, user=user)
        self.browser.get(self.live_server_url + '/staff/' + str(author.id))
        self.assertIn(author.user.first_name, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(author.about, body.text)


    def test_login_page(self):
        """
        login page test at /login
        """
        self.browser.get(self.live_server_url + '/login')
        self.assertIn('Login', self.browser.title)
        # create an author for login
        user = mommy.make(User, username='john')
        user.set_password('foopass')
        user.save()
        author = mommy.make(Author, user=user)
        # enter credentials
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(user.username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys('foopass')
        pass_field.submit()
        # should redirect to home
        self.assertIn('Home', self.browser.title)


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


    def test_items_model(self):
        """
        item model test
        """
        item = mommy.make(NewsItem)
        self.assertTrue(isinstance(item, NewsItem))
        self.assertTrue(isinstance(item.author, Author))
        item = mommy.make(BlogItem)
        self.assertTrue(isinstance(item, BlogItem))
        self.assertTrue(isinstance(item.author, Author))
        item = mommy.make(VideoItem)
        self.assertTrue(isinstance(item, VideoItem))
        self.assertTrue(isinstance(item.author, Author))
