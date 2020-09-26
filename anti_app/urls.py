from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='anti-start'),
    path('create/', views.page1, name="anti-create")
]
