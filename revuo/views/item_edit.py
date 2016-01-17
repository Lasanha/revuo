from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from revuo.forms import FormNewsItem, FormBlogItem, FormPublication
from revuo.models import NewsItem, BlogItem, Publication


class ItemEdit(View):
    template_name = 'revuo/edit_item.html'
    categories = {'N': FormNewsItem, 'B': FormBlogItem, 'P': FormPublication}
    classes = {'N': NewsItem, 'B': BlogItem, 'P': Publication}
    category = None

    @method_decorator(login_required)
    def get(self, request, category, item_id):
        item_class = self.classes[category]
        item_form = self.categories[category]
        instance = get_object_or_404(item_class, id=item_id, deleted=False, author=request.user.staff)
        form = item_form(instance=instance)
        return render(request, self.template_name, {'form': form}, context_instance=RequestContext(request))

    @method_decorator(login_required)
    def post(self, request, category, item_id):
        item_class = self.classes[category]
        item_form = self.categories[category]
        instance = get_object_or_404(item_class, id=item_id, deleted=False, author=request.user.staff)
        form = item_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(form.instance.get_url())
        return render(request, self.template_name, {'form': form}, context_instance=RequestContext(request))
