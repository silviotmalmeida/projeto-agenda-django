from django.contrib import admin
from .models import Categoria, Contato  # importando as models do app


# definindo as configurações de exibição da Categoria na área administrativa
class CategoriaAdmin(admin.ModelAdmin):

    # definindo as colunas a serem exibidas
    list_display = ('id', 'nome')

    # definindo em quais colunas serão colocados links de edição
    list_display_links = ('nome',)

    # definindo o limite de registros por página
    list_per_page = 10

    # definindo as colunas a serem consideradas no campo de pesquisa
    search_fields = ('nome',)


# definindo as configurações de exibição do Contato na área administrativa
class ContatoAdmin(admin.ModelAdmin):

    # definindo as colunas a serem exibidas
    list_display = ('id', 'nome', 'sobrenome', 'telefone',
                    'email', 'data_criacao', 'categoria')

    # definindo em quais colunas serão colocados links de edição
    list_display_links = ('nome',)

    # definindo em quais colunas serão criados filtros
    list_filter = ('categoria',)

    # definindo o limite de registros por página
    list_per_page = 10

    # definindo as colunas a serem consideradas no campo de pesquisa
    search_fields = ('nome',)


# registrando as models para exibição na área administrativa
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Contato, ContatoAdmin)
