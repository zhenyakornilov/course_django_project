from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main-page'),
    path('create-student/', views.CreateStudentView.as_view(), name='create-student'),
    path('generate-students/', views.GenerateStudentsView.as_view()),
    path('all-students/', views.StudentsListView.as_view(), name='all-students'),
    path('edit-student/<int:pk>/', views.EditStudentView.as_view(), name='edit-student'),
    path('delete-student/<int:pk>/', views.DeleteStudentView.as_view(), name='delete-student'),
    path('generate-students-form/', views.GenerateStudentsFormView.as_view(), name='generate-students-form')
]
