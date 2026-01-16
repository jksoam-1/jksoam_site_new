from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Apps
    path("", include("apps.home.urls")),
    path("blogs/", include("apps.blogs.urls")),
    path("learning/", include("apps.learning.urls")),
    path("questions/", include("apps.questions.urls")),
    path("devops/", include("apps.devops.urls")),
]

# Static & Media (development only)
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATICFILES_DIRS[0]
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
