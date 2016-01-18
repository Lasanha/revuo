from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View

from revuo.models import NewsItem, BlogItem, Publication

CACHE_NAME = getattr(settings, 'REVUO_CACHE_NAME', 'default')
CACHE_TIME = getattr(settings, 'REVUO_ITEM_VIEW_CACHE_TIME', 60)


class ItemView(View):
    categories = {'N': NewsItem, 'B': BlogItem, 'P': Publication}

    @method_decorator(cache_page(CACHE_TIME, cache=CACHE_NAME))
    def get(self, request, category, item_id):
        item_class = self.categories[category]
        if request.user.is_authenticated():
            item = get_object_or_404(item_class, id=item_id, deleted=False)
        else:
            item = get_object_or_404(item_class, id=item_id, authorized=True, deleted=False)
        template = 'revuo/{}_item.html'.format(category)
        return render(request, template, {'item': item, 'category': category})
