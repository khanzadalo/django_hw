from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from product.forms import ProductCreateForm, ReviewCreateForm, CategoryCreateForm
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
        CategoryCreateForm()
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


def product_detail_view(request, product_id):
    if request.method == 'GET':
        form = ReviewCreateForm()
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(
                request,
                'errors/404.html',
            )
        return render(
            request,
            'products/detail.html',
            context={'product': product, 'form': form}
        )
    elif request.method == 'POST':
        form = ReviewCreateForm(request.POST)

        if form.is_valid():
            Review.objects.create(product_id=product_id, **form.cleaned_data)
            return redirect(f'/products/{product_id}/')

        context = {
            'form': form
        }

        return render(
            request,
            'products/detail.html',
            context=context
        )


def product_create_view(request, product_id=None):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm()
        }

        return render(
            request,
            'products/create.html',
            context=context
        )

    elif request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect(f'/products/')

        context = {
            'form': form
        }

        return render(
            request,
            'products/create.html',
            context=context
        )


def category_create_view(request):
    if request.method == 'GET':
        context = {
            'form': CategoryCreateForm()
        }

        return render(
            request,
            'categories/create.html',
            context=context
        )

    elif request.method == 'POST':
        form = CategoryCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            form.save()
            return redirect('/products/')

        context = {
            'form': form
        }

        return render(
            request,
            'categories/create.html',
            context=context
        )


