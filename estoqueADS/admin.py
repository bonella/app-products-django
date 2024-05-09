from django.contrib import admin
from .models import Produtos
from .models import Categoria


class adminProdutos(admin.ModelAdmin):
    list_display = ['id', 'nome','preco','quantidade', 'em_estoque']
    list_filter = ['em_estoque']
    search_fields = ['nome']
    list_editable = ['quantidade']
    list_per_page = 5


admin.site.register(Produtos, adminProdutos)
admin.site.register(Categoria)

# MAKEMIGRATIONS
# MIGRATE