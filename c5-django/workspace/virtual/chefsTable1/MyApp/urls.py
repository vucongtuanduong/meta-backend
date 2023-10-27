from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_home', views.new_home, name='new_home'),
]