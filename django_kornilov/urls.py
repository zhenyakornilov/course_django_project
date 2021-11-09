"""students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("project-debug/", include(debug_toolbar.urls)),
    path("", include("students.urls")),
    path("", include("group.urls")),
    path("", include("teachers.urls")),
    path("", include("mail_processing.urls")),
    path("", include("currency.urls")),
    path("accounts/", include("user_signup.urls")),
]
handler404 = "students.views.handler404"
handler500 = "students.views.handler500"


admin.site.index_title = "Django Kornilov"
admin.site.site_header = "Django Kornilov Admin"
admin.site.site_title = "Admin panel"
