from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login_view)
]