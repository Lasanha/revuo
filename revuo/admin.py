from django.contrib import admin
from models import Author, NewsItem, BlogItem, VideoItem

admin.site.register(Author)
admin.site.register(NewsItem)
admin.site.register(VideoItem)
admin.site.register(BlogItem)
