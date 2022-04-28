from django.db import models


class Filme(models.Model):
    titulo = models.CharField(max_length= 100, unique=True)
    descricao = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    foto = models.ImageField(blank=True)



    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=30,unique=True)
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Acervo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE) #PODE NÃO EXISTIR AQUI ASS.: JOMOVA
    review_do_usuario = models.TextField(null=True, blank=True)




