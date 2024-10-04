from django.urls import path
from . import views
from kuwired_app import views as home

urlpatterns = [
    path('',home.home_view,name="home"),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('register/', views.register_view,name='register'),
    path('confirm/<uuid:confirmation_link>/', views.confirm_email, name='confirm_email'),
    path('registration/confirmation/', views.registration_confirmation, name='registration_confirmation'),  # New confirmation URL

  # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
   # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
   # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]































































































































































































































































































































































































                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 