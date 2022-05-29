"""PdE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import statistics
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from conf import settings

from apps.users.views import home
from apps.career.views import (list_careers, add_careers, edit_careers, list_semester_career, 
add_semester_career, edit_semester_career)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="index"),

    #Careers url's
    path('career/list', list_careers, name="list_careers"),
    path('career/add', add_careers, name="add_careers"),
    path('career/edit/<int:id>', edit_careers, name="edit_careers"),

    #Semester url's
    path('career=<int:id>/semester/list', list_semester_career, name="list_semester_career"),
    path('career=<int:id>/semester/add', add_semester_career, name="add_semester_career"),
    path('career/semester/edit/<int:id>', edit_semester_career, name="edit_semester_career"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
