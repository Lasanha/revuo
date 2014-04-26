from django.contrib import admin
from revuo.models import Author, NewsItem, BlogItem, VideoItem, Publication

admin.site.register(Author)
admin.site.register(NewsItem)
admin.site.register(VideoItem)
admin.site.register(BlogItem)
admin.site.register(Publication)
