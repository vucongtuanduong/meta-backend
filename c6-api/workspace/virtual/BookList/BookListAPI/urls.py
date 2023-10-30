from django.urls import path
from . import views


urlpatterns = [
# Add URL configuration for the path() function here
    path('books', views.books, name = 'book'),
    # path('./books/<int:pk>/', views.book_detail, name = 'book_detail')
]