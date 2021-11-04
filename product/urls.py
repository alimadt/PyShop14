from django.urls import path

from .views import *
from .class_views import *
urlpatterns = [

    path('', CategoryListView.as_view(), name='home'),
    path('<str:slug>/', ProductListView.as_view(), name='list'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/update/<int:product_id>/', ProductUpdateView.as_view(), name='product-update'),
    path('product/delete/<int:product_id>/', ProductDeleteView.as_view(), name='product-delete'),
    path('search', SearchListView.as_view(), name='search'),
]