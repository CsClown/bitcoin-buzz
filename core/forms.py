from .models import Reply, Post, UserProfile
from django import forms


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('content',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'topic', 'content']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
