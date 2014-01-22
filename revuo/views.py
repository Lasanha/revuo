from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from models import Item, Author, Publication


class Home(View):
    template_name = 'revuo/home.html'

    def get(self, request):
        return render(request, self.template_name, {})


class News(View):
    template_name = 'revuo/news.html'

    def get(self, request):
        news_list = Item.objects.filter(category='N')
        authorized = news_list.filter(authorized=True)
        ordered = authorized.order_by('-created_at')[:10]
        return render(request, self.template_name, {'news_list':ordered})


class NewsItem(View):
    template_name = 'revuo/news_item.html'

    def get(self, request, news_id):
        news_item = get_object_or_404(Item, id=news_id, authorized=True)
        return render(request, self.template_name, {'news_item':news_item})


class Media(View):
    template_name = 'revuo/media.html'

    def get(self, request):
        media_list = Item.objects.filter(category='V')
        authorized = media_list.filter(authorized=True)
        ordered = authorized.order_by('-created_at')[:10]
        return render(request, self.template_name, {'media_list':ordered})


class MediaItem(View):
    template_name = 'revuo/media_item.html'

    def get(self, request, media_id):
        media_item = get_object_or_404(Item, id=media_id, authorized=True)
        return render(request, self.template_name, {'media_item':media_item})


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


class Blog(View):
    template_name = 'revuo/blog.html'

    def get(self, request):
        post_list = Item.objects.filter(category='B')
        authorized = post_list.filter(authorized=True)
        ordered = authorized.order_by('-created_at')[:10]
        return render(request, self.template_name, {'post_list':ordered})


class BlogItem(View):
    template_name = 'revuo/blog_item.html'

    def get(self, request, post_id):
        blog_item = get_object_or_404(Item, id=post_id, authorized=True)
        return render(request, self.template_name, {'blog_item':blog_item})
