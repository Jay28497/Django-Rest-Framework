from django.urls import path
from FunctionBaseAPIView import views

urlpatterns = [
    path('customer/', views.customer_list),
    path('customer/<int:pk>', views.customer_detail),
]
