from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from revuo.models import NewsItem, VideoItem, BlogItem, Author, Publication
from revuo.forms import FormNewsItem, FormVideoItem, FormBlogItem, FormEditProfile


class Home(View):
    template_name = 'revuo/home.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ItemList(View):
    categories = {'news': NewsItem, 'media': VideoItem, 'blog': BlogItem}

    def get(self, request, category):
        Item = self.categories[category]
        item_list = Item.objects.filter(authorized=True)
        ordered = item_list.order_by('-created_at')[:10]
        template = 'revuo/{}.html'.format(category)
        return render(request, template, {'items_list':ordered})


class ItemView(View):
    categories = {'N': NewsItem, 'V': VideoItem, 'B': BlogItem}

    def get(self, request, category, item_id):
        Item = self.categories[category]
        if request.user.is_authenticated():
            item = get_object_or_404(Item, id=item_id)
        else:
            item = get_object_or_404(Item, id=item_id, authorized=True)
        template = 'revuo/{}_item.html'.format(category)
        return render(request, template, {'item':item})


class Publications(View):
    template_name = 'revuo/publications.html'

    def get(self, request):
        authorized = Publication.objects.filter(authorized=True)
        ordered = authorized.order_by('-created_at')[:10]
        return render(request, self.template_name, {'pubs_list':ordered})


class Staff(View):
    template_name = 'revuo/staff.html'

    def get(self, request):
        authors_list = Author.objects.all()
        return render(request, self.template_name, {'authors_list':authors_list})


class StaffView(View):
    template_name = 'revuo/staff_view.html'

    def get(self, request, staff_id):
        author = get_object_or_404(Author, id=staff_id)
        return render(request, self.template_name, {'author':author})


# ===========================
# logged actions
# ===========================


class NewItem(View):
    template_name = 'revuo/new_item.html'
    categories = {'N': FormNewsItem, 'V': FormVideoItem, 'B': FormBlogItem}

    @method_decorator(login_required)
    def get(self, request, category):
        FormItem = self.categories[category]
        form = FormItem()
        return render(request, self.template_name, {'form': form},
            context_instance=RequestContext(request))


    @method_decorator(login_required)
    def post(self, request, category):
        FormItem = self.categories[category]
        form = FormItem(request.POST, request.FILES)
        if form.is_valid():
            item = form.instance
            author = Author.objects.get(user=request.user)
            item.author = author
            item.authorized = True
            item.save()
            return redirect('/')
        return render(request, self.template_name, {'form': form},
            context_instance=RequestContext(request))


class Publisher(View):
    template_name = 'revuo/publisher.html'

    """
    gets a list of items pending authorization
    """
    @method_decorator(login_required)
    def get(self, request):
        news = NewsItem.objects.filter(authorized=False)
        posts = BlogItem.objects.filter(authorized=False)
        videos = VideoItem.objects.filter(authorized=False)
        items_list = list(news) + list(posts) + list(videos)
        return render(request, self.template_name, {'items_list':items_list},
            context_instance=RequestContext(request))


class EditProfile(View):
    template_name = 'revuo/edit_item.html'

    @method_decorator(login_required)
    def get(self, request):
        author_info = Author.objects.get(user=request.user)
        form = FormEditProfile(instance=author_info)
        return render(request, self.template_name, {'form': form},
            context_instance=RequestContext(request))


    @method_decorator(login_required)
    def post(self, request):
        author_info = Author.objects.get(user=request.user)
        form = FormEditProfile(request.POST, request.FILES, instance=author_info)
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        return render(request, self.template_name, {'form': form},
            context_instance=RequestContext(request))
