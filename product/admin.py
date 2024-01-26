from django.contrib import admin

# Register your models here.
from product.models import Product, Category, Review


admin.site.register(Product)