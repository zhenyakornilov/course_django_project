from django.urls import path
from .import views

urlpatterns = [
    path('all-teachers/', views.show_all_teachers),
    path('generate-teachers/', views.generate_teachers)
]