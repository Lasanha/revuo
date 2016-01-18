from django.conf import settings
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View

from revuo.models import NewsItem, BlogItem, Publication

CACHE_NAME = getattr(settings, 'REVUO_CACHE_NAME', 'default')
CACHE_TIME = getattr(settings, 'REVUO_ITEM_LIST_CACHE_TIME', 60)


class ItemList(View):
    categories = {'news': NewsItem, 'blog': BlogItem, 'publications': Publication}
    category = None

    @method_decorator(cache_page(CACHE_TIME, cache=CACHE_NAME))
    def get(self, request):
        item_class = self.categories[self.category]
        item_list = item_class.objects.filter(authorized=True, deleted=False)
        ordered = item_list.order_by('-created_at')[:10]
        template = 'revuo/{}.html'.format(self.category)
        return render(request, template, {'items_list': ordered})

