from django.contrib import auth
from django.shortcuts import render
from .models import Product, Category
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required


# Create your views here.



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
            category = get_object_or_404(Category,slug=category_slug)
            products = products.filter(category=category)
    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    print(page)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
            products = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)

    return render(request,'products/product_list.html', {'category':category,'categories':categories,'products':products,'page':page})


@login_required(login_url='/dashboard/login/')

def product_detail(request,id,slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/product_detail.html',{'product':product,'cart_product_form':cart_product_form,})

