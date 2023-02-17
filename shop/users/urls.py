from django.urls import path, include
from users.views import Register
from . import views

app_name = 'shop' 

urlpatterns= [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),

    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
    name='product_list_by_category'
    ),
    path('<int:id>/<slug:slug>', views.product_detail,
    name='product_detail')
]