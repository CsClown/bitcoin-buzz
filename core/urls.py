from django.urls import path
from . import views as core_views

urlpatterns =[
    path('', core_views.PostList.as_view(), name='home'),
    path('<slug:slug>/', core_views.conversation, name='conversation'),
    path('<slug:slug>/delete_reply/<int:reply_id>', core_views.reply_delete, name='reply_delete'),
]
