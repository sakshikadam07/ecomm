from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import Cartitem
from carts.views import _cart_id
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def store(request, category_slug=None):
    categories  = None
    products    = None

    total_count = 0

    if category_slug != None:
        categories      = get_object_or_404(Category, slug=category_slug)
        products        = Product.objects.filter(category=categories, is_available=True)
        product_count   = products.count()
        total_count     =+ product_count


    else:
        products = Product.objects.all().filter(is_available=True)


    context = {
        'products': products,
        'total_count' : total_count,

    }

    return render(request,'store/store.html', context)

    # single view for category products

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = Cartitem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Exception as e:
        raise e

    context = {
        'single_product' : single_product,
        'in_cart' : in_cart,
    }
    return render(request, 'store/product_detail.html', context)

def search(request):
    if 'Keyword' in request.GET:
        Keyword = request.GET['Keyword']
        if Keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=Keyword)| Q( product_name__icontains=Keyword))
            product_count = products.count()
            context = {
                'products' : products,
                'product_count': product_count,
            }
    return render(request,'store/store.html', context)
