from django.shortcuts import render, redirect
from products.models import Product
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def product(request):
    error = ''
    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop')
        else:
            error = 'Форма неверная'

    context: {
        'product': Product.objects.all(),
    }
    form = ProductForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'products/product.html', data)

def shop(request):
    productlist = Product.objects.all()
    return render(request, 'products/shop.html', {'productlist': productlist})