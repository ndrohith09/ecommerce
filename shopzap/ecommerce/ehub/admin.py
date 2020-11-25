from django.contrib import admin

# Register your models here.
from .models import Product,productpage

admin.site.register(Product)
admin.site.register(productpage)