from django.contrib import admin

# Register your models here.
from .models import Product,fashion,test

admin.site.register(Product)
admin.site.register(fashion)
admin.site.register(test)