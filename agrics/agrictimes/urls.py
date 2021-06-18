from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name ='agrictimes'

urlpatterns = [
    path('',views.product_list, name='product_list'),
    path('<slug:category_slug>/',views.product_list, name ='product_list_by_category'),
    path('<int:id>/<slug:slug>/',views.product_detail, name='product_detail'),
    #path('login/', views.user_login, name='login'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]