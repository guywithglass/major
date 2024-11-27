from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('product/', views.product, name='product'),
    path('about/', views.about, name='about'),
    path('contract/', views.contract, name='contract'),
    path('contract_view/', views.contract_view, name='contract_view'),
    path('accept_contract/<int:id>/', views.accept_contract, name='accept_contract'),
]
