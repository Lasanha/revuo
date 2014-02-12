from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from model_mommy import mommy
from models import Author, Admin, NewsItem, BlogItem, VideoItem, Publication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class PortalTest(LiveServerTestCase):
    username = 'john'
    userpass = 'foopas'

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        # create an author for restricted tests
        user = mommy.make(User, username=self.username, first_name='John')
        user.set_password(self.userpass)
        user.save()
        self.author = mommy.make(Author, user=user)


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
        # create a new one via form
        # enter credentials
        self.browser.get(self.live_server_url + '/login')
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.userpass)
        pass_field.submit()
        # go to form
        self.browser.get(self.live_server_url + '/restricted/N/add')
        title_field = self.browser.find_element_by_name('title')
        title_field.send_keys('news item')
        desc_field = self.browser.find_element_by_name('description')
        desc_field.send_keys('news description')
        text_field = self.browser.find_element_by_name('text')
        text_field.send_keys('news text body')
        text_field.submit()
        # go to news list and look for the title
        self.browser.get(self.live_server_url + '/news')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('news item', body.text)


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
        # create a new one via form
        # enter credentials
        self.browser.get(self.live_server_url + '/login')
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.userpass)
        pass_field.submit()
        # go to form
        self.browser.get(self.live_server_url + '/restricted/V/add')
        title_field = self.browser.find_element_by_name('title')
        title_field.send_keys('video item')
        desc_field = self.browser.find_element_by_name('video')
        desc_field.send_keys('http://example.org')
        text_field = self.browser.find_element_by_name('text')
        text_field.send_keys('video text body')
        text_field.submit()
        # go to video list and look for the title
        self.browser.get(self.live_server_url + '/media')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('video item', body.text)


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
        # create a new one via form
        # enter credentials
        self.browser.get(self.live_server_url + '/login')
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.userpass)
        pass_field.submit()
        # go to form
        self.browser.get(self.live_server_url + '/restricted/B/add')
        title_field = self.browser.find_element_by_name('title')
        title_field.send_keys('blog item')
        desc_field = self.browser.find_element_by_name('description')
        desc_field.send_keys('blog description')
        text_field = self.browser.find_element_by_name('text')
        text_field.send_keys('blog text body')
        text_field.submit()
        # go to blog list and look for the title
        self.browser.get(self.live_server_url + '/blog')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('blog item', body.text)


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
        # staff view
        self.browser.get(self.live_server_url + '/staff/' + str(self.author.id))
        self.assertIn(self.author.user.first_name, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(self.author.about, body.text)
        # enter credentials
        self.browser.get(self.live_server_url + '/login')
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.userpass)
        pass_field.submit()
        # go to form
        self.browser.get(self.live_server_url + '/restricted/editprofile')
        about_field = self.browser.find_element_by_name('about')
        about_field.send_keys('new about')
        about_field.submit()
        # go to staff view and look for new about
        self.browser.get(self.live_server_url + '/staff/' + str(self.author.id))
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('new about', body.text)
        # change password
        self.browser.get(self.live_server_url + '/restricted/password/change')
        curr_field = self.browser.find_element_by_name('old_password')
        curr_field.send_keys(self.userpass)
        new1_field = self.browser.find_element_by_name('new_password1')
        new1_field.send_keys('newpasswd')
        new2_field = self.browser.find_element_by_name('new_password2')
        new2_field.send_keys('newpasswd')
        new2_field.submit()
        # try passwords
        user_wrong = authenticate(username=self.username, password=self.userpass)
        user_right = authenticate(username=self.username, password='newpasswd')
        self.assertFalse(user_wrong)
        self.assertTrue(user_right)


    def test_login_page(self):
        """
        login page test at /login
        """
        self.browser.get(self.live_server_url + '/login')
        self.assertIn('Login', self.browser.title)
        # enter credentials
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.userpass)
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
