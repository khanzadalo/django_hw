from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from product.forms import ProductCreateForm, ReviewCreateForm, CategoryCreateForm
from product.models import Product, Category, Review
from shop import settings


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = settings.PAGE_SIZE

    def get_queryset(self):
        queryset = super().get_queryset()
        selected_category = self.request.GET.get('category')
        search = self.request.GET.get('search')
        order = self.request.GET.get('order')

        if selected_category:
            category = get_object_or_404(Category, title=selected_category)
            queryset = queryset.filter(category=category)
        elif search:
            queryset = queryset.filter(Q(title__icontains=search))

        if order == 'title':
            queryset = queryset.order_by('title')
        elif order == '-title':
            queryset = queryset.order_by('-title')
        elif order == 'created_at':
            queryset = queryset.order_by('created_at')
        elif order == '-created_at':
            queryset = queryset.order_by('-created_at')
        else:
            queryset = queryset.exclude(user=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = self.request.GET.get('category')
        context['categories'] = Category.objects.all()
        return context


class ProductDitailView(DetailView):
    model = Product
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['review_form'] = ReviewCreateForm
        context['has_change_permission'] = (context['product'].user == self.request.user)
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/create.html'
    success_url = '/products/'

    def get_absolute_url(self):
        if self.request.user.is_authenticated:
            return reverse('products_list')
        return reverse('login')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreateForm
    pk_url_kwarg = 'product_id'
    template_name = 'products/update.html'
    success_url = '/products/'

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        if product.user != request.user:
            return HttpResponse('Permission denied', status=403)
        return super().get(request, *args, **kwargs)


class ProductDeleteView(DetailView):
    model = Product
    template_name = 'products/delete.html'
    pk_url_kwarg = 'product_id'
    success_url = '/products.html'


class CategoriesListView(ListView):
    model = Category
    template_name = 'categories/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoryCreateForm()
        context['categories'] = Category.objects.all()
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'categories/create.html'

    def get_success_url(self):
        return '/products/'

    def form_invalid(self, form):
        context = {'form': form}
        return render(self.request, self.template_name, context)


class CategoryProductsView(TemplateView):
    template_name = 'categories/category_products.html'
    pk_url_kwarg = 'category_id'

    def get_context_data(self, category_id, **kwargs):
        category = get_object_or_404(Category, id=category_id)
        products = category.products.all()

        context = {
            'category': category,
            'products': products,
        }
        return context

    def get(self, request, category_id):
        context = self.get_context_data(category_id)
        return self.render_to_response(context)
