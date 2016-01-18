from django.conf import settings
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View

from revuo.models import Staff

CACHE_NAME = getattr(settings, 'REVUO_CACHE_NAME', 'default')
CACHE_TIME = getattr(settings, 'REVUO_STAFF_LIST_CACHE_TIME', 60)


class StaffList(View):
    @method_decorator(cache_page(CACHE_TIME, cache=CACHE_NAME))
    def get(self, request):
        authors_list = Staff.objects.all().order_by('user__username')
        template = 'revuo/staff.html'
        return render(request, template, {'authors_list': authors_list})

