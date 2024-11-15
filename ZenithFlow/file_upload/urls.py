from django.contrib import admin
from django.urls import path
from file_upload import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.File_Upload_View),
]
