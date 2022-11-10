from django.urls import path
from . import views
# from django.conf.urls import url


urlpatterns = [
    path('', views.mainpage, name="main"),
    path('product_info/<str:pk>', views.product_detail, name="product_info"),
    path('category_page/<str:pk>', views.category_page, name ='category_page'),
]