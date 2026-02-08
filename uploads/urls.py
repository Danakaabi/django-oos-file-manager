from django.urls import path
from . import views


# ======================================
# URL PATTERNS - UPLOADS APP
# ======================================
urlpatterns = [
    # الصفحة الرئيسية لرفع الملفات
    # مثال:
    # http://8.213.84.133:8000/
    path("", views.upload_file, name="upload"),

    # صفحة نجاح رفع الملف
    # مثال:
    # http://8.213.84.133:8000/success/1/
    path(
        "success/<int:pk>/",
        views.upload_success,
        name="upload_success"
    ),
]
