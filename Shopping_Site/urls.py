from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('website.urls')),
    path('item/', include('item.urls')),
    path('inbox/', include('conversation.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
