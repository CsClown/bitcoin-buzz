from django.contrib import admin
from .models import Post, Topic, Reply

# Register your models here.
admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Reply)
