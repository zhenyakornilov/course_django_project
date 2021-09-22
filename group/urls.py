from django.urls import path

from .import views

urlpatterns = [
    path('all-groups/', views.GroupListView.as_view(), name='all-groups'),
    path('create-group/', views.CreateGroupView.as_view()),
]
