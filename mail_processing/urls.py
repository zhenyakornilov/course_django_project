from django.urls import path

from . import views

urlpatterns = [
    path('contact-us/', views.show_contact_form, name='contact-us')
]
