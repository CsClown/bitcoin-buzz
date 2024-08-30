from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Topic, Reply, UserProfile


# Register your models here.
admin.site.unregister(Group)


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)  # slug is created automatically


admin.site.register(Post, PostAdmin)
admin.site.register(Topic)
admin.site.register(Reply)
admin.site.register(UserProfile)
