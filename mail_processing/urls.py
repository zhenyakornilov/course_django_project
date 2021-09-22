from django.urls import path

from . import views

urlpatterns = [
    path('contact-us/', views.ShowContactFormView.as_view(), name='contact-us'),
]
