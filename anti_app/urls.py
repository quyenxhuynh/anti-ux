from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='anti-start'),
    path('create/', views.create, name="anti-create"),
    path('time/', views.time, name="anti-time"),
    path('test/', views.test, name="anti-test"),

    path('instructions/', views.instructions, name="anti-instructions"),
    path('shop/', views.store, name="anti-store"),
    path('cart/', views.cart, name="anti-cart"),
    path('checkout/', views.checkout, name="anti-checkout")
]
