from django.contrib.auth import views as auth_view
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),
    path('login/', views.AuthenticateView.as_view(), name='login'),
    path('logout/', views.LoginFormView.as_view(), name='logout'),
    path('password-change/', auth_view.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/',
         auth_view.PasswordChangeDoneView.as_view(), name='password_change_done')
]
