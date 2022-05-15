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
from apps.career.views import list_careers, add_careers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="index"),

    #Careers urls
    path('career/list', list_careers, name="list_careers"),
    path('career/add', add_careers, name="add_careers"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
