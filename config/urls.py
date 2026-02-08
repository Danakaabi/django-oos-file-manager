from django.contrib import admin
from django.urls import path, include

# إعدادات خاصة بالملفات المرفوعة (MEDIA)
from django.conf import settings
from django.conf.urls.static import static


# ======================================
# URL PATTERNS
# ======================================
urlpatterns = [
    # لوحة تحكم Django Admin
    path('admin/', admin.site.urls),

    # ربط تطبيق uploads بالمسار الرئيسي
    # أي طلب يروح "/" يتم توجيهه لـ uploads/urls.py
    path('', include('uploads.urls')),
]


# ======================================
# SERVING MEDIA FILES (Development Only)
# ======================================
# هذا الجزء يسمح لـ Django بعرض الملفات المرفوعة
# فقط أثناء التطوير (DEBUG = True)
# في Production (ECS + Nginx) لن نستخدمه
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
