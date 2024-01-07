from django.shortcuts import get_object_or_404, render

from store.models import Product
from category.models import Category

# Create your views here.


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(categories=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {"products": products, "product_count": product_count}
    return render(request, "store/store.html", context)


def product_detail(request, category_slug, product_slug):
    # product = get_object_or_404(Product, slug=product_slug)
    # context = {"product": product}
    product = get_object_or_404(
        Product,
        categories__slug=category_slug,
        slug=product_slug,
    )
    context = {"product": product}
    return render(request, "store/product_detail.html", context)
