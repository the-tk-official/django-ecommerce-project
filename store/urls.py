from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>/products/', views.category_list, name='category_list'),
]
