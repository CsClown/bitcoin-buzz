from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from .models import Post, Topic, Reply, UserProfile


# Register your models here.
admin.site.unregister(Group)


# Unregister the social account models
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)


# Unregister the Site model from the sites framework
admin.site.unregister(Site)


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)  # slug is created automatically


admin.site.register(Post, PostAdmin)
admin.site.register(Topic)
admin.site.register(Reply)
admin.site.register(UserProfile)
