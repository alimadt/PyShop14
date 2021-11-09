from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


@login_required()  # куда перенаправится, если юзер не зашел; прописали в settings LOGIN_URL
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("list", product.category.slug)


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    return render(request, 'cart/cart-detail.html')

# from django.shortcuts import render, get_object_or_404, redirect
#
# # Create your views here.
# from .forms import CreateProductForm, UpdateProductForm
# from .models import Category, Product
#
#
# def home_page(request):
#     categories = Category.objects.all()
#     print(categories)
#     return render(request, 'home1.html', {"categories":categories})
#
#
# def product_list(request,slug):
#     products = Product.objects.filter(category__slug = slug)
#     return render(request, 'product_list.html', locals())
#
#
# def product_detail(request, product_id):
#     # product = Product.objects.get(id=product_id)
#     product = get_object_or_404(Product, pk=product_id)
#     return render(request, 'detail.html', locals())
#
# def product_create(request):
#     if request.method == 'POST':
#         print(request.POST)
#         product_form = CreateProductForm(request.POST, request.FILES)
#
#         if product_form.is_valid():
#             product = product_form.save()
#             return redirect('detail', product.id)
#
#     else:
#         product_form = CreateProductForm()
#     return render(request, 'create_product.html', locals())
#
# def product_update(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     product_form = UpdateProductForm(request.POST or None, request.FILES or None, instance=product)
#
#     if product_form.is_valid():
#         product_form.save()
#         return redirect('detail', product_id)
#
#     return render(request, 'update_product.html', locals())
#
# def product_delete(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     if request.method == 'POST':
#         product.delete()
#         slug = product.category.slug
#         return redirect('list', slug)
#     return render(request, 'delete_product.html', locals())
