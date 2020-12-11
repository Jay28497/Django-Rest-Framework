from django.urls import path
from API import views

urlpatterns = [
    path('products', views.products_list),
    path('products/<int:pk>', views.products_detail),
    path('products/published', views.products_list_published),
]
