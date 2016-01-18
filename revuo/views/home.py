from django.conf import settings
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View

CACHE_NAME = getattr(settings, 'REVUO_CACHE_NAME', 'default')
CACHE_TIME = getattr(settings, 'REVUO_HOME_CACHE_TIME', 60)


class Home(View):
    template_name = 'revuo/home.html'

    @method_decorator(cache_page(CACHE_TIME, cache=CACHE_NAME))
    def get(self, request):
        return render(request, self.template_name, {})
