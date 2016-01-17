from django.views.generic import View
from django.shortcuts import render

from revuo.models import NewsItem, BlogItem, Publication


class ItemList(View):
    categories = {'news': NewsItem, 'blog': BlogItem, 'publications': Publication}
    category = None

    def get(self, request):
        item_class = self.categories[self.category]
        item_list = item_class.objects.filter(authorized=True, deleted=False)
        ordered = item_list.order_by('-created_at')[:10]
        template = 'revuo/{}.html'.format(self.category)
        return render(request, template, {'items_list': ordered})

