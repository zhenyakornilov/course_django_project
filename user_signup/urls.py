from django.contrib.auth import views as auth_view
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),
    path('login/', views.AuthenticateView.as_view(), name='login'),
    path('logout/', views.LoginFormView.as_view(), name='logout'),
    path('password-change/', views.PassChangeView.as_view(), name='password_change'),
    path('password-change-success/',
         auth_view.PasswordChangeDoneView.as_view(
             template_name='user_signup/password_change_done.html'), name='password_change_done'
         ),
    path('password-reset/',
         auth_view.PasswordResetView.as_view(template_name='user_signup/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_view.PasswordResetDoneView.as_view(template_name='user_signup/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(template_name='user_signup/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_view.PasswordResetCompleteView.as_view(template_name='user_signup/password_reset_complete.html'),
         name='password_reset_complete')
]
