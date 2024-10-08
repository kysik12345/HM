
from django.urls import path
from mysite.views import *

urlpatterns = [
    path('', index, name='index'),
    path('show/<int:pk>', show, name='show'),
    path('add/', add, name='add'),
    path('about/', about, name='about'),
    path('delete/<int:pk>', delete, name='delete'),
    path('edit/<int:pk>', edit, name='edit'),
]

