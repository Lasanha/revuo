from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from revuo.models import NewsItem, BlogItem, Publication


class Dashboard(View):
    template_name = 'revuo/dashboard.html'

    """
    list/search for bulk action on items
    """
    @method_decorator(login_required)
    def get(self, request):
        news = NewsItem.objects.order_by('-created_at').filter(deleted=False)
        posts = BlogItem.objects.order_by('-created_at').filter(deleted=False)
        pubs = Publication.objects.order_by('-created_at').filter(deleted=False)

        # TODO: check editor rights
        # news = news.filter(author=request.user.staff)
        # posts = posts.filter(author=request.user.staff)
        # pubs = pubs.filter(author=request.user.staff)

        news_paginator = Paginator(news, 10)
        posts_paginator = Paginator(posts, 10)
        pubs_paginator = Paginator(pubs, 10)
        page = request.GET.get('page', 1)

        try:
            news = news_paginator.page(page)
        except PageNotAnInteger:
            news = news_paginator.page(1)
        except EmptyPage:
            news = news_paginator.page(news_paginator.num_pages)
        try:
            posts = posts_paginator.page(page)
        except PageNotAnInteger:
            posts = posts_paginator.page(1)
        except EmptyPage:
            posts = posts_paginator.page(posts_paginator.num_pages)
        try:
            pubs = pubs_paginator.page(page)
        except PageNotAnInteger:
            pubs = pubs_paginator.page(1)
        except EmptyPage:
            pubs = pubs_paginator.page(pubs_paginator.num_pages)

        current_page = max(news.number, posts.number, pubs.number)
        previous_page = current_page - 1
        next_page = current_page + 1
        num_pages = max(news.paginator.num_pages, posts.paginator.num_pages, pubs.paginator.num_pages)

        multi_page_info = {
            'has_previous': previous_page > 0,
            'previous_page': previous_page,
            'has_next': current_page < num_pages,
            'next_page': next_page,
            'current': current_page,
            'num_pages': num_pages,
        }

        sections = [
            {'section': 'News', 'items': news},
            {'section': 'Blog Posts', 'items': posts},
            {'section': 'Publications', 'items': pubs},
        ]
        return render(request, self.template_name, {'sections': sections, 'multi_page_info': multi_page_info},
                      context_instance=RequestContext(request))
