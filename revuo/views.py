from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.base import View
from revuo.models import NewsItem, BlogItem, Author, Publication
from revuo.forms import FormNewsItem, FormBlogItem, FormEditProfile, FormPublication
import json


class Home(View):
    template_name = 'revuo/home.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ItemList(View):
    categories = {'news': NewsItem, 'blog': BlogItem, 'publications': Publication}
    category = None

    def get(self, request):
        Item = self.categories[self.category]
        item_list = Item.objects.filter(authorized=True)
        ordered = item_list.order_by('-created_at')[:10]
        template = 'revuo/{}.html'.format(self.category)
        return render(request, template, {'items_list':ordered})


class ItemView(View):
    categories = {'N': NewsItem, 'B': BlogItem, 'P': Publication}

    def get(self, request, category, item_id):
        Item = self.categories[category]
        if request.user.is_authenticated():
            item = get_object_or_404(Item, id=item_id)
        else:
            item = get_object_or_404(Item, id=item_id, authorized=True)
        template = 'revuo/{}_item.html'.format(category)
        return render(request, template, {'item':item, 'category':category})


class Staff(View):
    template_name = 'revuo/staff.html'

    def get(self, request):
        authors_list = Author.objects.all()
        return render(request, self.template_name, {'authors_list':authors_list})


class StaffView(View):
    template_name = 'revuo/staff_view.html'

    def get(self, request, staff_id):
        author = get_object_or_404(Author, id=staff_id)
        return render(request, self.template_name, {'author':author})


# ===========================
# logged actions
# ===========================


class NewItem(View):
    template_name = 'revuo/new_item.html'
    categories = {'N': FormNewsItem, 'B': FormBlogItem, 'P': FormPublication}
    category = None

    @method_decorator(login_required)
    def get(self, request):
        FormItem = self.categories[self.category]
        form = FormItem()
        return render(request, self.template_name, {'form': form},
            context_instance=RequestContext(request))


    @method_decorator(login_required)
    def post(self, request):
        FormItem = self.categories[self.category]
        form = FormItem(request.POST, request.FILES)
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            if self.category == 'P': # need to find out why it didn't work for ModelForm
                item = Publication(author=author,attachment=request.FILES['attachment'])
                item.title = form.cleaned_data['title']
                item.description = form.cleaned_data['description']
            else:
                item = form.instance
                item.author = author
                item.authorized = False
            item.save()
            return redirect(item.get_url())
        return render(request, self.template_name, {'form': form},
            context_instance=RequestContext(request))


def editor_test(user):
    return Author.objects.get(user=user).editor


class Publisher(View):
    template_name = 'revuo/publisher.html'

    """
    gets a list of items pending authorization
    """
    @method_decorator(login_required)
    @method_decorator(user_passes_test(editor_test))
    def get(self, request):
        news = NewsItem.objects.filter(authorized=False)
        posts = BlogItem.objects.filter(authorized=False)
        pubs = Publication.objects.filter(authorized=False)
        items_list = list(news) + list(posts) + list(pubs)
        return render(request, self.template_name, {'items_list':items_list},
            context_instance=RequestContext(request))


class PublishItem(View):
    categories = {'N': NewsItem, 'B': BlogItem, 'P': Publication}

    @method_decorator(login_required)
    @method_decorator(user_passes_test(editor_test))
    def get(self, request, category, item_id):
        if request.is_ajax():
            Item = self.categories[category]
            item = get_object_or_404(Item, id=int(item_id))
            item.authorize()
            item.save()
            result = {'msg': 'Item Published'}
        else:
            return HttpResponseForbidden("FORBIDDEN")
        return HttpResponse(json.dumps(result), content_type='application/json')


class TrashItem(View):
    categories = {'N': NewsItem, 'B': BlogItem, 'P': Publication}

    @method_decorator(login_required)
    @method_decorator(user_passes_test(editor_test))
    def get(self, request, category, item_id):
        if request.is_ajax():
            Item = self.categories[category]
            item = get_object_or_404(Item, id=int(item_id))
            item.delete()
            result = {'msg': 'Item Deleted'}
        else:
            return HttpResponseForbidden("FORBIDDEN")
        return HttpResponse(json.dumps(result), content_type='application/json')


class EditProfile(View):
    template_name = 'revuo/edit_item.html'

    @method_decorator(login_required)
    def get(self, request):
        author_info = Author.objects.get(user=request.user)
        form = FormEditProfile(instance=author_info)
        return render(request, self.template_name, {'form': form},
            context_instance=RequestContext(request))


    @method_decorator(login_required)
    def post(self, request):
        author_info = Author.objects.get(user=request.user)
        form = FormEditProfile(request.POST, request.FILES, instance=author_info)
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        return render(request, self.template_name, {'form': form},
            context_instance=RequestContext(request))
