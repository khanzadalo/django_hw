from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from product.models import Product, Category, Review


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def current_date(request):
    now = datetime.now()
    current_data = now.strftime("%Y-%m-%d")
    if request.method == 'GET':
        return HttpResponse(f"today is the {current_data}")


def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodby user!")


def product_view(request):
    if request.method == 'GET':
        selected_category = request.GET.get('category')
        if selected_category:
            category = get_object_or_404(Category, title=selected_category)
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()

        context = {'products': products}

        return render(
            request,
            'products/products.html',
            context=context
        )


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(
            request,
            'categories/list.html',
            {"categories": categories}
        )


def category_products_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    products = category.products.all()

    context = {
        'category': category,
        'products': products,
    }
    return render(request,
                  'categories/category_products.html',
                  context)
