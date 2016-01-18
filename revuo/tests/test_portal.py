from django.test import LiveServerTestCase
from selenium import webdriver
from model_mommy import mommy
from revuo.models import Staff, NewsItem, BlogItem, Publication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from time import sleep
import os


class PortalTest(LiveServerTestCase):
    staff_username = 'john'
    staff_pass = 'foopas'

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        # create an author and an editor for restricted tests
        user = mommy.make(User, username=self.staff_username, first_name='John')
        user.set_password(self.staff_pass)
        user.save()
        self.author = mommy.make(Staff, user=user)

    def tearDown(self):
        self.browser.quit()

    def _enter_credentials(self):
        # enter credentials
        self.browser.get(self.live_server_url + reverse('revuo:login'))
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.staff_username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.staff_pass)
        pass_field.submit()

    def test_home_page(self):
        """
        home page test at /
        """
        self.browser.get(self.live_server_url + reverse('revuo:home'))
        self.assertIn('Home', self.browser.title)

    def test_create_news_page(self):
        """
        news creation form
        """
        self._enter_credentials()
        # go to form
        self.browser.get(self.live_server_url + reverse('revuo:add_news'))
        title_field = self.browser.find_element_by_name('title')
        title_field.send_keys('news item')
        # switch to editor frame
        ed_frame = self.browser.find_elements_by_tag_name("iframe")[0]
        self.browser.switch_to.frame(ed_frame)
        text_field = self.browser.find_element_by_class_name('note-editable')
        text_field.send_keys('news text body')
        sleep(3)
        # go back
        # if I enter the description first, the text field becomes empty and the test fails... why?
        self.browser.switch_to.default_content()
        desc_field = self.browser.find_element_by_name('description')
        desc_field.send_keys('news description')
        desc_field.submit()
        # redirected to the item
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Pending Authorization', body.text)

    def test_news_list_page(self):
        """
        news page test at /news
        """
        # create some news
        mommy.make(NewsItem, authorized=True, _quantity=10)
        # then check the page
        self.browser.get(self.live_server_url + reverse('revuo:news'))
        self.assertIn('News', self.browser.title)
        news_list = self.browser.find_element_by_name('news_list')
        news_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(news_list)
        self.assertIsNotNone(news_item)

    def test_news_view_page(self):
        # news view
        news = mommy.make(NewsItem, authorized=True)
        self.browser.get(self.live_server_url + news.get_url())
        self.assertIn(news.title, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(news.description, body.text)
        self.assertIn(news.text, body.text)

    def test_create_publication_page(self):
        self._enter_credentials()
        # go to form
        self.browser.get(self.live_server_url + reverse('revuo:add_publication'))
        title_field = self.browser.find_element_by_name('title')
        title_field.send_keys('publication')
        desc_field = self.browser.find_element_by_name('description')
        desc_field.send_keys('pub description')
        file_field = self.browser.find_element_by_css_selector('input[type="file"]')
        file_field.send_keys(os.path.abspath(__file__))
        desc_field.submit()
        # redirected to the item
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Pending Authorization', body.text)
        self.assertIn('pub description', body.text)

    def test_publications_page(self):
        """
        news page test at /publications
        """
        # create publications
        mommy.make(Publication, authorized=True, _quantity=10)
        # check page
        self.browser.get(self.live_server_url + reverse('revuo:publications'))
        self.assertIn('Publications', self.browser.title)
        pubs_list = self.browser.find_element_by_name('pubs_list')
        pubs_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(pubs_list)
        self.assertIsNotNone(pubs_item)

    def test_publication_view_page(self):
        publication = mommy.make(Publication, authorized=True)
        self.browser.get(self.live_server_url + publication.get_url())
        self.assertIn(publication.title, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(publication.description, body.text)

    def test_create_blog_entry_page(self):
        self._enter_credentials()
        # go to form
        self.browser.get(self.live_server_url + reverse('revuo:add_blog'))
        title_field = self.browser.find_element_by_name('title')
        title_field.send_keys('blog item')
        # switch to editor frame
        ed_frame = self.browser.find_elements_by_tag_name("iframe")[0]
        self.browser.switch_to.frame(ed_frame)
        text_field = self.browser.find_element_by_class_name('note-editable')
        text_field.send_keys('blog text body')
        sleep(3)
        # go back - see news test
        self.browser.switch_to.default_content()
        desc_field = self.browser.find_element_by_name('description')
        desc_field.send_keys('blog description')
        desc_field.submit()
        # redirected to the item
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Pending Authorization', body.text)

    def test_blog_page(self):
        """
        news page test at /blog
        """
        # create some media
        mommy.make(BlogItem, authorized=True, _quantity=10)
        # aaaand check page
        self.browser.get(self.live_server_url + reverse('revuo:blog'))
        self.assertIn('Blog', self.browser.title)
        posts_list = self.browser.find_element_by_name('post_list')
        posts_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(posts_list)
        self.assertIsNotNone(posts_item)

    def test_blog_entry_view_page(self):
        blog_entry = mommy.make(BlogItem, authorized=True)
        self.browser.get(self.live_server_url + blog_entry.get_url())
        self.assertIn(blog_entry.title, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(blog_entry.description, body.text)
        self.assertIn(blog_entry.text, body.text)

    def test_staff_page(self):
        """
        news page test at /staff
        """
        # create some users
        mommy.make(Staff, _quantity=10)
        # aaaand check page
        self.browser.get(self.live_server_url + reverse('revuo:staff'))
        self.assertIn('Staff', self.browser.title)
        authors_list = self.browser.find_element_by_name('authors_list')
        authors_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(authors_list)
        self.assertIsNotNone(authors_item)

    def test_staff_view_page(self):
        # staff view
        self.browser.get(self.live_server_url + self.author.get_url())
        self.assertIn(self.author.user.first_name, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(self.author.about, body.text)

    def test_staff_edit_about(self):
        self._enter_credentials()
        # go to form
        self.browser.get(self.live_server_url + reverse('revuo:staff_edit'))
        about_field = self.browser.find_element_by_name('about')
        about_field.send_keys('new about')
        about_field.submit()
        # go to staff view and look for new about
        self.browser.get(self.live_server_url + self.author.get_url())
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('new about', body.text)

    def test_staff_change_password(self):
        self._enter_credentials()
        # change password
        self.browser.get(self.live_server_url + '/restricted/password/change')
        curr_field = self.browser.find_element_by_name('old_password')
        curr_field.send_keys(self.staff_pass)
        new1_field = self.browser.find_element_by_name('new_password1')
        new1_field.send_keys('newpasswd')
        new2_field = self.browser.find_element_by_name('new_password2')
        new2_field.send_keys('newpasswd')
        new2_field.submit()
        # try passwords
        user_wrong = authenticate(username=self.staff_username, password=self.staff_pass)
        user_right = authenticate(username=self.staff_username, password='newpasswd')
        self.assertFalse(user_wrong)
        self.assertTrue(user_right)

    def test_publisher_page(self):
        # creating unauthorized items
        news = mommy.make(NewsItem, authorized=False, deleted=False)
        post = mommy.make(BlogItem, authorized=False, deleted=False)
        # login
        self._enter_credentials()
        # go to publisher page, should see Pending Items
        self.browser.get(self.live_server_url + reverse('revuo:dashboard'))
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(news.title, body.text)
        self.assertIn(post.title, body.text)

    def test_publisher_delete_item(self):
        news = mommy.make(NewsItem, authorized=False, deleted=False)
        self._enter_credentials()
        self.browser.get(self.live_server_url + news.get_url())
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Pending', body.text)
        # click on delete
        self.browser.find_element_by_name('delete').click()
        # wait deletion
        sleep(3)
        # assert object was deleted
        news = NewsItem.objects.filter(id=news.id, deleted=False)
        self.assertFalse(news)

    def test_publisher_authorize_item(self):
        # authorize this
        post = mommy.make(BlogItem, authorized=False, deleted=False)
        self._enter_credentials()
        self.browser.get(self.live_server_url + post.get_url())
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Pending', body.text)
        # click on authorize
        self.browser.find_element_by_name('authorize').click()
        # wait reload
        sleep(3)
        # make sure that post is now authorized
        post = BlogItem.objects.get(id=post.id)
        self.assertTrue(post.authorized)
        
    def test_login_page(self):
        """
        login page test at /login
        """
        self.browser.get(self.live_server_url + reverse('revuo:login'))
        self.assertIn('Login', self.browser.title)
        self._enter_credentials()
        # should redirect to home
        self.assertIn('Home', self.browser.title)
