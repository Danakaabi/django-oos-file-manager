from pathlib import Path

# ======================================
# BASE DIRECTORY
# ======================================
# المسار الأساسي للمشروع (root directory)
BASE_DIR = Path(__file__).resolve().parent.parent


# ======================================
# MEDIA FILES (User Uploads)
# ======================================
# رابط الوصول للملفات المرفوعة
MEDIA_URL = "/media/"

# المسار الفعلي لتخزين الملفات محليًا
MEDIA_ROOT = BASE_DIR / "media"


# ======================================
# SECURITY SETTINGS
# ======================================
# ⚠️ مفتاح سري للتشفير (لا ترفعيه على GitHub)
# لاحقًا سننقله إلى .env
SECRET_KEY = 'django-insecure-d&e3-+-&lr!jmeufj9yx&@qejn$f^azqwu=d74@aa!nv^tqr)#'

# وضع التطوير
# True = تطوير
# False = Production
DEBUG = True

# السماح بالوصول للتطبيق
# محليًا فقط
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# ======================================
# APPLICATION DEFINITION
# ======================================
INSTALLED_APPS = [
    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom app
    "uploads.apps.UploadsConfig",
]


# ======================================
# MIDDLEWARE
# ======================================
# طبقات معالجة الطلبات (Request / Response)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',      # أمان أساسي
    'django.contrib.sessions.middleware.SessionMiddleware',  # الجلسات
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',           # حماية CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # تسجيل الدخول
    'django.contrib.messages.middleware.MessageMiddleware',     # الرسائل
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # حماية iframe
]


# ======================================
# URL & TEMPLATE CONFIG
# ======================================
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ======================================
# WSGI (Deployment)
# ======================================
WSGI_APPLICATION = 'config.wsgi.application'


# ======================================
# DATABASE
# ======================================
# قاعدة بيانات SQLite (مناسبة للتطوير)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ======================================
# PASSWORD VALIDATION
# ======================================
# قواعد أمان كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ======================================
# INTERNATIONALIZATION
# ======================================
# اللغة الافتراضية (قياسي للمشاريع السحابية)
LANGUAGE_CODE = 'en-us'

# التوقيت العالمي (أفضل خيار للسيرفرات)
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True


# ======================================
# STATIC FILES (CSS, JS, Images)
# ======================================
# رابط الملفات الثابتة
STATIC_URL = 'static/'

# المسار النهائي بعد collectstatic
# مهم جدًا عند النشر على ECS + Nginx
STATIC_ROOT = BASE_DIR / "staticfiles"
