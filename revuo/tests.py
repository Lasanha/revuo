from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from model_mommy import mommy
from revuo.models import Author, Admin, NewsItem, BlogItem, Publication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from time import sleep
import os


class PortalTest(LiveServerTestCase):
    username = 'john'
    ed_username = 'editor'
    userpass = 'foopas'

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        # create an author and an editor for restricted tests
        user = mommy.make(User, username=self.username, first_name='John')
        ed_user = mommy.make(User, username=self.ed_username, first_name='Editor')
        user.set_password(self.userpass)
        ed_user.set_password(self.userpass)
        user.save()
        ed_user.save()
        self.author = mommy.make(Author, user=user)
        self.editor = mommy.make(Author, user=ed_user, editor=True)


    def tearDown(self):
        self.browser.quit()


    def test_home_page(self):
        """
        home page test at /
        """
        self.browser.get(self.live_server_url + reverse('revuo:home'))
        self.assertIn('Home', self.browser.title)


    def test_news_page(self):
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
        # news view
        news = mommy.make(NewsItem, authorized=True)
        self.browser.get(self.live_server_url + news.get_url())
        self.assertIn(news.title, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(news.description, body.text)
        self.assertIn(news.text, body.text)
        # create a new one via form
        # enter credentials
        self.browser.get(self.live_server_url + reverse('revuo:login'))
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.userpass)
        pass_field.submit()
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
        # create a new one via form
        # enter credentials
        self.browser.get(self.live_server_url + reverse('revuo:login'))
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.userpass)
        pass_field.submit()
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
        # post view
        post = mommy.make(BlogItem, authorized=True)
        self.browser.get(self.live_server_url + post.get_url())
        self.assertIn(post.title, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(post.description, body.text)
        self.assertIn(post.text, body.text)
        # create a new one via form
        # enter credentials
        self.browser.get(self.live_server_url + reverse('revuo:login'))
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.userpass)
        pass_field.submit()
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


    def test_staff_page(self):
        """
        news page test at /staff
        """
        # create some users
        mommy.make(Author, _quantity=10)
        # aaaand check page
        self.browser.get(self.live_server_url + reverse('revuo:staff'))
        self.assertIn('Staff', self.browser.title)
        authors_list = self.browser.find_element_by_name('authors_list')
        authors_item = self.browser.find_element_by_tag_name('li')
        self.assertIsNotNone(authors_list)
        self.assertIsNotNone(authors_item)
        # staff view
        self.browser.get(self.live_server_url + self.author.get_url())
        self.assertIn(self.author.user.first_name, self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(self.author.about, body.text)
        # enter credentials
        self.browser.get(self.live_server_url + reverse('revuo:login'))
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.userpass)
        pass_field.submit()
        # go to form
        self.browser.get(self.live_server_url + reverse('revuo:edit_profile'))
        about_field = self.browser.find_element_by_name('about')
        about_field.send_keys('new about')
        about_field.submit()
        # go to staff view and look for new about
        self.browser.get(self.live_server_url + self.author.get_url())
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


    def test_publisher_page(self):
        # creating unauthorized items
        news = mommy.make(NewsItem, authorized=False)
        post = mommy.make(BlogItem, authorized=False)
        # login
        self.browser.get(self.live_server_url + reverse('revuo:login'))
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.userpass)
        pass_field.submit()
        # go to publisher page, redirects to login
        self.browser.get(self.live_server_url + reverse('revuo:publisher'))
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Username', body.text)
        # editor logs in
        user_field = self.browser.find_element_by_name('username')
        user_field.send_keys(self.ed_username)
        pass_field = self.browser.find_element_by_name('password')
        pass_field.send_keys(self.userpass)
        pass_field.submit()
        # go to publisher page, should see Pending Items
        self.browser.get(self.live_server_url + reverse('revuo:publisher'))
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(news.title, body.text)
        self.assertIn(post.title, body.text)
        # and visiting to see them pending and authorize or delete
        # just look
        self.browser.get(self.live_server_url + news.get_url())
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Pending', body.text)
        # click on delete
        self.browser.find_element_by_name('delete').click()
        # wait deletion
        sleep(3)
        # assert object was deleted
        news = NewsItem.objects.filter(id=news.id)
        self.assertFalse(news)

        # authorize this
        self.browser.get(self.live_server_url + post.get_url())
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Pending', body.text)
        # click on authorize
        self.browser.find_element_by_name('authorize').click()
        # wait reload
        sleep(3)
        # make sure that post is now authorized
        post = BlogItem.objects.get(id=post.id) # why do I need to refresh the reference?
        self.assertTrue(post.authorized)
        

    def test_login_page(self):
        """
        login page test at /login
        """
        self.browser.get(self.live_server_url + reverse('revuo:login'))
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
            author.__str__(),
            ' '.join([author.user.first_name, author.user.last_name])
            )


    def test_admin_model(self):
        """
        admin model test
        """
        admin = mommy.make(Admin)
        self.assertTrue(isinstance(admin, Admin))
        self.assertEqual(
            admin.__str__(),
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
