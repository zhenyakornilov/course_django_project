from django.urls import path

from . import views

urlpatterns = [
    path('all-teachers/', views.TeachersListView.as_view(), name='all-teachers'),
    path('create-teacher/', views.CreateTeacherView.as_view(), name='create-teacher'),
    path('edit-teacher/<int:pk>', views.EditTeacherView.as_view(), name='edit-teacher'),
    path('delete-teacher/<int:pk>', views.DeleteTeacherView.as_view(), name='delete-teacher'),
]
