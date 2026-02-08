from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_file, name="upload"),
    path("success/<int:pk>/", views.upload_success, name="upload_success"),
]
