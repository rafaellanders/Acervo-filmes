from django.contrib import admin
from App_acervo.models import Filme, Usuario, Acervo


class ModeloTestes(admin.ModelAdmin):
    list_display = ('titulo',)




admin.site.register(Filme, ModeloTestes)
admin.site.register(Usuario)
admin.site.register(Acervo)

# Register your models here.
