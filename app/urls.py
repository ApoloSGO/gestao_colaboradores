from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pessoas.urls')),  # Rotas do app pessoas
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from . import views

urlpatterns = [
    path('', views.lista_colaboradores, name='lista_colaboradores'),
    path('novo/', views.novo_colaborador, name='novo_colaborador'),
    path('admin/', admin.site.urls),
    path('', include('pessoas.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
