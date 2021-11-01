from django.contrib.auth import views as auth_view
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),
    path('login/', views.AuthenticateView.as_view(), name='login'),
    path('logout/', views.LoginFormView.as_view(), name='logout'),
    path('password-change/', views.PassChangeView.as_view(), name='password_change'),
    path('password-changed/',
         auth_view.PasswordChangeDoneView.as_view(
             template_name='user_signup/password_change_done.html'), name='password_change_done'
         )
]
