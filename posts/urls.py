from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login')
]