from django.shortcuts import render
from django.views.generic.base import View

class Home(View):
    template_name = 'revuo/home.html'

    def get(self, request):
        return render(request, self.template_name, {})


class News(View):
    template_name = 'revuo/news.html'

    def get(self, request):
        return render(request, self.template_name, {})


class Media(View):
    template_name = 'revuo/media.html'

    def get(self, request):
        return render(request, self.template_name, {})


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
        return render(request, self.template_name, {})