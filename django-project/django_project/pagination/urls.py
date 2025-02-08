from django.urls import path
from .views import item_list, contact_view, contact_success_view, product_list, review_success_view

urlpatterns = [
    path('items/', item_list, name='item_list'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
    path('products/', product_list, name='product_list'),
    path('review/success/', review_success_view, name='review_success'),
]