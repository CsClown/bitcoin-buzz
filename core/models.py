from django.db import models
from django.utils.text import slugify #chatgpt suggestion of auto-slugs
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=200)

    def get_topic_posts_count(self):
        return self.topic_posts.count()

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, related_name="topic_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    #chat gpt suggestion of auto-slugs
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_replies")
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_replies")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

