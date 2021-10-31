from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),
    path('login/', views.AuthenticateView.as_view(), name='login'),
    path('logout/', views.LoginFormView.as_view(), name='logout')
]
