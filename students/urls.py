from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page),
    path('create-student/', views.create_student),
    path('generate-students/', views.generate_students),
    path('all-students/', views.show_all_students, name='all-students'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit-student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete-student'),
]
