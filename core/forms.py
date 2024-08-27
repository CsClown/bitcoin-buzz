from .models import Reply, Post
from django import forms


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('content',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'topic', 'content']