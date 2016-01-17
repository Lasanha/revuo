from django.views.generic import View
from django.shortcuts import render


class Home(View):
    template_name = 'revuo/home.html'

    def get(self, request):
        return render(request, self.template_name, {})
