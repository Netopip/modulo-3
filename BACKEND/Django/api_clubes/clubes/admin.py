from django.contrib import admin
from clubes.models import Clube,Jogador

# Register your models here.
#classe de configuração

class ClubeAdmin(admin.ModelAdmin):
    list_display = ['nome','uf']
    list_filter = ['uf']
    search_fields = ['nome']
    

    
admin.site.register(Clube,ClubeAdmin)
    


class JogadorAdmin(admin.ModelAdmin):
    list_display = ['nome','numero']
    list_filter = ['numero']
    search_fields = ['nome']

admin.site.register(Jogador, JogadorAdmin)