from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("apps.book.urls")),
    # path('api/books/', include("apps.book.urls")),
    # path("api/users/", include("apps.book.user_urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
