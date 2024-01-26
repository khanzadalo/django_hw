from django.contrib import admin
from django.urls import path
from product.views import (hello_view, goodby_view, current_date,
                           main_page_view, product_view, categories_list_view,)

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', main_page_view),
    path('hello/', hello_view),
    path('goodby/', goodby_view),
    path('date/', current_date),
    path('products/', product_view),

    path('categories/', categories_list_view),

]
