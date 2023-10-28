from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('new_home', views.new_home, name='new_home'),

    path('menu_item/10', views.display_menu_item),
    re_path(r'^menu_item/([0-9]{2})/$', views.display_menu_item),
    
]