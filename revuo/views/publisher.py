from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.base import View
from revuo.models import NewsItem, BlogItem, Publication
from revuo.models import Staff


def editor_test(user):
    return Staff.objects.get(user=user).editor


class Publisher(View):
    template_name = 'revuo/publisher.html'

    """
    gets a list of items pending authorization
    """
    @method_decorator(login_required)
    @method_decorator(user_passes_test(editor_test))
    def get(self, request):
        news = NewsItem.objects.filter(authorized=False, deleted=False)
        posts = BlogItem.objects.filter(authorized=False, deleted=False)
        pubs = Publication.objects.filter(authorized=False, deleted=False)
        items_list = list(news) + list(posts) + list(pubs)
        return render(request, self.template_name, {'items_list': items_list}, context_instance=RequestContext(request))
