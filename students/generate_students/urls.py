from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('generate-student/', views.generate_one_student),
    path('generate-students/', views.generate_students),
    path('all-students/', views.show_all_students),
]
