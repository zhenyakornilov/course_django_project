from django.urls import path

from . import views

urlpatterns = [
    path('all-teachers/', views.TeachersListView.as_view(), name='all-teachers'),
    path('create-teacher/', views.create_teacher, name='create-teacher'),
    path('edit-teacher/<int:teacher_id>', views.edit_teacher, name='edit-teacher'),
    path('delete-teacher/<int:teacher_id>', views.delete_teacher, name='delete-teacher'),
]
