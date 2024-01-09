"""
URL configuration for stackoverflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from stackusers import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('stackbase.urls')),
    path('register/',user_view.register,name="register"), # Register User
    path('login/', auth_views.LoginView.as_view(template_name="stackusers/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="stackusers/logout.html"), name="logout"),
    path('profile/', user_view.profile, name="profile"),
    path('profile/update/', user_view.profile_update, name="profile_update"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
