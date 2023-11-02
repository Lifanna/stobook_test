
from . import  views
from .views import *
from django.urls import path

urlpatterns = [
    path('', main,name='home'),
    path('book',book,name='book'),
    path('order',order,name='order'),
    path('login',login,name='login')
]
