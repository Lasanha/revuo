from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from models import Item, Author, Publication


class Home(View):
    template_name = 'revuo/home.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ItemList(View):
    categories = {'news': 'N', 'media': 'V', 'blog': 'B'}

    def get(self, request, category):
        item_list = Item.objects.filter(category=self.categories[category])
        authorized = item_list.filter(authorized=True)
        ordered = authorized.order_by('-created_at')[:10]
        template = 'revuo/{}.html'.format(category)
        return render(request, template, {'items_list':ordered})


class ItemView(View):

    def get(self, request, category, item_id):
        item = get_object_or_404(Item, category=category, id=item_id, authorized=True)
        template = 'revuo/{}_item.html'.format(category)
        return render(request, template, {'item':item})


class Publications(View):
    template_name = 'revuo/publications.html'

    def get(self, request):
        authorized = Publication.objects.filter(authorized=True)
        ordered = authorized.order_by('-created_at')[:10]
        return render(request, self.template_name, {'pubs_list':ordered})


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
