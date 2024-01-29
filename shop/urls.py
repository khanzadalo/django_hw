from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from product.views import hello_view, goodby_view, current_date, \
    main_page_view, product_view, categories_view, category_products_view

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', main_page_view),
    path('hello/', hello_view),
    path('goodby/', goodby_view),
    path('date/', current_date),
    path('products/', product_view),

    path('categories/', categories_view),
    path('categories/<int:category_id>/', category_products_view, name='category_products'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
