from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View

from revuo.models import Staff

CACHE_NAME = getattr(settings, 'REVUO_CACHE_NAME', 'default')
CACHE_TIME = getattr(settings, 'REVUO_STAFF_VIEW_CACHE_TIME', 60)


class StaffView(View):
    @method_decorator(cache_page(CACHE_TIME, cache=CACHE_NAME))
    def get(self, request, staff_id):
        author = get_object_or_404(Staff, id=staff_id)
        template = 'revuo/staff_view.html'
        return render(request, template, {'author': author})
