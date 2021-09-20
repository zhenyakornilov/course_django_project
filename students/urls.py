from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPage.as_view()),
    path('create-student/', views.create_student, name='create-student'),
    path('generate-students/', views.generate_students),
    path('all-students/', views.StudentsListView.as_view(), name='all-students'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit-student'),
    path('delete-student/<int:pk>/', views.DeleteStudentView.as_view(), name='delete-student'),
    path('generate-students-form/', views.generate_students_from_from, name='generate-students-form')
]
