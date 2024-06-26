from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from rezume.views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='index.html')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
