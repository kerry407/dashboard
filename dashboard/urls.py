from django.urls import path 
from . import views 
from user import views as user_views

urlpatterns = [
    path('', views.account, name='account'),
    path('payment/', views.payment, name='deposit'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.loginform, name='login'),
    path('contact/', views.contact, name='contact'),
    path('logout/', user_views.logoutuser, name='logout'),
    path('passwordchange/', user_views.change_password, name='change_password')
]
