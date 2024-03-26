"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from app import views as app_views
from users import views as user_views
from django.contrib.auth import views as auth_views
from app.admin import Natalie_site

urlpatterns = [
    path("", app_views.homepage, name="homepage"),
    path("register/", user_views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        user_views.log_out,
        name="logout",
    ),
    path("admin/", Natalie_site.urls),
]
# shows website title in the index
admin.site.index_title = "Natalie Turner Therapy"
# changes header Title in the admin
admin.site.site_header = "Natalie Turner's Admin"
# changes tab title
admin.site.site_title = "Admin"