from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View

from revuo.models import Publication, Staff
from revuo.forms import FormNewsItem, FormBlogItem, FormPublication


class ItemNew(View):
    template_name = 'revuo/new_item.html'
    categories = {'N': FormNewsItem, 'B': FormBlogItem, 'P': FormPublication}
    category = None

    @method_decorator(login_required)
    def get(self, request):
        item_form = self.categories[self.category]
        form = item_form()
        return render(request, self.template_name, {'form': form}, context_instance=RequestContext(request))

    @method_decorator(login_required)
    def post(self, request):
        item_form = self.categories[self.category]
        form = item_form(request.POST, request.FILES)
        if form.is_valid():
            author = request.user.staff
            if self.category == 'P': # need to find out why it didn't work for ModelForm
                item = Publication(author=author, attachment=request.FILES['attachment'])
                item.title = form.cleaned_data['title']
                item.description = form.cleaned_data['description']
            else:
                item = form.instance
                item.author = author
                item.authorized = False
            item.save()
            return redirect(item.get_url())
        return render(request, self.template_name, {'form': form}, context_instance=RequestContext(request))
