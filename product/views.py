from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import CreateProductForm, UpdateProductForm
from .models import Category, Product


def home_page(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'home1.html', {"categories":categories})

def product_list(request,slug):
    products = Product.objects.filter(category__slug = slug)
    return render(request, 'product_list.html', locals())

def product_detail(request, product_id):
    # product = Product.objects.get(id=product_id)
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', locals())

def product_create(request):
    if request.method == 'POST':
        print(request.POST)
        product_form = CreateProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            product = product_form.save()
            return redirect('detail', product.id)

    else:
        product_form = CreateProductForm()
    return render(request, 'create_product.html', locals())

def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_form = UpdateProductForm(request.POST or None, request.FILES or None, instance=product)

    if product_form.is_valid():
        product_form.save()
        return redirect('detail', product_id)

    return render(request, 'update_product.html', locals())

def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        slug = product.category.slug
        return redirect('list', slug)
    return render(request, 'delete_product.html', locals())