
from django.contrib import admin
from django.urls import path, include
from catalogo.views import index, productos, contacto, home, productos_filtrados
from django.conf.urls.static import static
from django.conf import settings

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('productos/', productos, name='productos'),
    path('productos/<str:categoria>/', productos_filtrados, name='productos_filtrados'),
    path('catalogo', include('catalogo.urls')),  # o la ruta correcta para tu aplicación
    path('contacto/', contacto, name='contacto'),
    path('', home, name='home'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('usuarios.urls')),
    path('carrito/', include('carrito.urls')),
    path('venta/', include('venta.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
