from django.urls import path
from . import views as core_views

urlpatterns =[
    path('', core_views.PostList.as_view(), name='home'),
    path('create/', core_views.post_create, name='post_create'),
    path('topics/', core_views.TopicList.as_view(), name='topic_list'),  
    path('topics/<int:pk>/', core_views.TopicPostList.as_view(), name='topic_posts'),
    path('<slug:slug>/', core_views.conversation, name='conversation'),
    path('<slug:slug>/delete_reply/<int:reply_id>', core_views.reply_delete, name='reply_delete'),
    path('<slug:slug>/delete_post/<int:post_id>', core_views.post_delete, name='post_delete'),
    path('post/<slug:slug>/like/', core_views.like_post, name='like_post'),
    
]
