from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts', views.accounts, name='accounts'),
    path('accounts/new', views.create_account, name='create-account'),
    path('accounts/<int:id>/update', views.update_account, name='update-account'),
    path('accounts/<int:id>/delete', views.delete_account, name='delete-account')
]