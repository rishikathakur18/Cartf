from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'ShopHome'),
    path('about/',views.about, name = 'AboutUs'),
    path('contact/',views.contact, name = 'ContactUs'),
    path('tracker/', views.tracker, name='Tracker'),
    path('search/', views.search, name='Search'),
    path("products/<int:myid>", views.productView, name="ProductView"), #here we can't use any whitespace between angle brackets
    path('checkout/', views.checkout, name='Checkout'),
    # path('handlerequest/', views.handlerequest, name='HandleRequest'),

]