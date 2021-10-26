"""django_aws3 URL Configuration


"""
from django.conf import settings  # new
from django.conf.urls.static import static  # new
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')), # new
    path('', include('django_aws3_app.urls')),  # new
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
