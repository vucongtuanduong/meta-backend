from rest_framework import serializers
from LittleLemonAPI.models import User, Article, Tag, Comment, Category, Link, FriendLink, Carousel, Banner

from decimal import Decimal

from .models import User, Article, Tag, Comment, Category, Link, FriendLink, Carousel, Banner, \
    Cart, Order, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']