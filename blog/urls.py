# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('COVID19Korea/', views.COVID19_map_data, name='COVID19_map_data'),
]