from django.shortcuts import render
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
        products = Product.objects.all()  # QuerySet

        context = {'products': products}

        return render(
            request,
            'products/products.html',
            context=context
        )


def categories_list_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        return render(
            request,
            'categories/list.html',
            {"categories": categories}
        )