from django.urls import path
from myapp2 import views

urlpatterns = [
    path('client_orders/', views.client_orders, name='client_orders'),
]