from django.shortcuts import render
from django.views.generic.base import View
from models import Item

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


class Media(View):
    template_name = 'revuo/media.html'

    def get(self, request):
        media_list = Item.objects.filter(category='V')
        authorized = media_list.filter(authorized=True)
        ordered = authorized.order_by('-created_at')[:10]
        return render(request, self.template_name, {'media_list':ordered})


class Publications(View):
    template_name = 'revuo/publications.html'

    def get(self, request):
        return render(request, self.template_name, {})


class Staff(View):
    template_name = 'revuo/staff.html'

    def get(self, request):
        return render(request, self.template_name, {})


class Blog(View):
    template_name = 'revuo/blog.html'

    def get(self, request):
        post_list = Item.objects.filter(category='B')
        authorized = post_list.filter(authorized=True)
        ordered = authorized.order_by('-created_at')[:10]
        return render(request, self.template_name, {'post_list':ordered})
