from django.shortcuts import render
from django.views.generic.base import View

class Home(View):
    template_name = 'revuo/home.html'

    def get(self, request):
        return render(request, self.template_name, {})
