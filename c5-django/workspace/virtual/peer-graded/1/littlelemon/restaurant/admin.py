from django.contrib import admin

# Register your models here.
from .models import Menu  # Import the Menu model from your models.py file

# Register the Menu model with the admin interface
admin.site.register(Menu)