from django.views.generic import View
from django.shortcuts import get_object_or_404, render

from revuo.models import NewsItem, BlogItem, Publication


class ItemView(View):
    categories = {'N': NewsItem, 'B': BlogItem, 'P': Publication}

    def get(self, request, category, item_id):
        item_class = self.categories[category]
        if request.user.is_authenticated():
            item = get_object_or_404(item_class, id=item_id, deleted=False)
        else:
            item = get_object_or_404(item_class, id=item_id, authorized=True, deleted=False)
        template = 'revuo/{}_item.html'.format(category)
        return render(request, template, {'item': item, 'category': category})
