from rest_framework import serializers
from App_acervo.models import Filme, Usuario, Acervo

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome']

class UsuarioSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class AcervoSerializer(serializers.ModelSerializer):
    class Meta:

        model = Acervo
        fields='__all__'

class ListaFilmesVistosSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.nome')
    filme = serializers.ReadOnlyField(source = 'filme.titulo')
    class Meta:
        model = Acervo
        fields = ['usuario','filme']
