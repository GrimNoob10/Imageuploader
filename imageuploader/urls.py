from django.contrib import admin
from django.urls import path
from myapp import views
# Image uploader

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home)
] + (static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)) 
#   url pattern to find the media files from the data base

