from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.base import View

from revuo.models import NewsItem, BlogItem, Publication
from .utils import editor_test

import json


class ItemPublish(View):
    categories = {'N': NewsItem, 'B': BlogItem, 'P': Publication}

    @method_decorator(login_required)
    @method_decorator(user_passes_test(editor_test))
    def get(self, request, category, item_id):
        if request.is_ajax():
            item_class = self.categories[category]
            item = get_object_or_404(item_class, id=int(item_id), deleted=False)
            item.authorize()
            item.save()
            result = {'msg': 'Item Published'}
        else:
            return HttpResponseForbidden("FORBIDDEN")
        return HttpResponse(json.dumps(result), content_type='application/json')

