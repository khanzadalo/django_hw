from django.urls import path
from .views import (main_page_view, ProductsListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
                    ProductDitailView, CategoriesListView, CategoryCreateView, CategoryProductsView)
app_name = 'product'


urlpatterns = [
    path('', main_page_view, name='main'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/<pk>/', ProductDitailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='create_product'),
    path('products/<pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('products/<pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<pk>/', CategoryProductsView.as_view(), name='category_products'),

]
