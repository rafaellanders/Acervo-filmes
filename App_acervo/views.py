from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from App_acervo.serializers import FilmeSerializer,UsuarioSerializer,AcervoSerializer,ListaFilmesVistosSerializer, UsuarioSerializerPost
from App_acervo.models import Filme,Usuario,Acervo
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
'''
class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
'''
class FilmeViewset(viewsets.ModelViewSet):
    """ Listando todos os filmes """

    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class UsuarioViewset(viewsets.ModelViewSet):
    """ Listando todos os usuarios"""

    queryset = Usuario.objects.all()


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UsuarioSerializerPost

        return UsuarioSerializer


class AcervoViewset(viewsets.ModelViewSet):
    """Listando todos os filmes cadastrados pelos usuarios"""
    queryset = Acervo.objects.all()
    serializer_class = AcervoSerializer

class ListaFilmesVistos(generics.ListAPIView):


    def get_queryset(self):
        queryset = Acervo.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset


    serializer_class = ListaFilmesVistosSerializer