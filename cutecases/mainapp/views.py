from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *


def mainpage(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, "mainapp/index.html", context)


def product_detail(request, pk):
    product = Product.objects.get(id = pk)
    form = OrderCreateForm()
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заказ принят")
            return redirect("main")

    else:
        form = OrderCreateForm()


    context = {
        'product': product,
        'form': form
    }
    return render(request, "mainapp/single-product.html", context)


def category_page(request, pk):
    products = Product.objects.filter(device=pk)
    context = {
        'products': products,
    }
    return render(request, "mainapp/index.html", context)

