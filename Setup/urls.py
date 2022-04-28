

from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from App_acervo.views import FilmeViewset, UsuarioViewset, AcervoViewset, ListaFilmesVistos #,LoginView
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
router.register('Filmes', FilmeViewset)
router.register('Usuario', UsuarioViewset)
router.register('Acervo', AcervoViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('usuario/<int:pk>/acervo/',ListaFilmesVistos.as_view()),
   # path('login/',LoginView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
