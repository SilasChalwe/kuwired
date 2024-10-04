from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="kuwired-home"),
    path('contact/',views.contact_view,name="contact_us"),
    path('contact/success',views.contact_sent_view,name="kuwired-contact-success"),
    path('about/',views.about_view,name="kuwired-about"),
    path('services/',views.services_view,name="kuwired-services"),
    path('product/',views.products_list_view,name="kuwired-products-list"),
    path('products/product/<int:product_id>',views.products_list_view,name="kuwired-products"),
    path('team/',views.team_view,name="kuwired-team"),
]
