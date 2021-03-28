from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products/', views.product, name='products'),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
