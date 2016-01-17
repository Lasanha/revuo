from django.contrib import admin
from revuo.models import Staff
from revuo.models import NewsItem, BlogItem, Publication


admin.site.register(Staff)
admin.site.register(NewsItem)
admin.site.register(BlogItem)
admin.site.register(Publication)
