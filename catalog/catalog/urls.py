from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.conf.urls.static import static

# from . import settings
from django.conf import settings
=======
>>>>>>> 4b18188892c36b6b01568f971ad0f2cd895fdbbf


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls", namespace="products")),
<<<<<<< HEAD
    path("", include("accounts.urls", namespace="accounts")),
    path("captcha/", include("captcha.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======
    path("", include("accounts.urls")),
    path("captcha/", include("captcha.urls"))
]
>>>>>>> 4b18188892c36b6b01568f971ad0f2cd895fdbbf
