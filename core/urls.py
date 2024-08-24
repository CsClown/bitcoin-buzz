from django.urls import path
from . import views as core_views

urlpatterns =[
    path('', core_views.index, name='index')
]
