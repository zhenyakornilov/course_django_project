from django.urls import path

from .import views

urlpatterns = [
    path('all-groups/', views.show_all_groups, name='all-groups'),
    path('create-group/', views.create_group),
]
