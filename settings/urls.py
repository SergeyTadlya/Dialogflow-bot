from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(route="admin/", view=admin.site.urls),
    path(route='accounts/', view=include('allauth.urls')),
    path(route='', view=include('bot.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)