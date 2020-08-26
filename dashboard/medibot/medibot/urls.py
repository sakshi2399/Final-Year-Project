"""medibot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from dashboard.views import index,report,rep_generatoion,register, pdf_downloader, sec_master
from dashboard.views import *
# from .router import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', index , name ='index'),
    path ('report',report, name='report')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
