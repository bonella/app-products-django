from django.shortcuts import render, HttpResponse, redirect
from .models import Produtos
from .models import Categoria
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def index(request):
    produtos = Produtos.objects.filter(criador_id=request.user.id)
    return render(request, 'pages/index.html', {'produtos':produtos})

@login_required(redirect_field_name='login')
def adicionar_produto(request):

    if request.method == "POST":
        nome = request.POST['nome']
        imagem = request.FILES.get('image')
        preco = request.POST['preco']
        descricao = request.POST['descricao']
        quantidade = request.POST['quantidade']
        categoria = request.POST['categoria']
        codigo = request.POST['codigo']
        em_estoque = False
        print(type(imagem))
        print(imagem)
        if int(quantidade) > 0:
            em_estoque = True 
        data_criacao = datetime.now()
        Produtos.objects.create(
            criador_id=request.user.id,
            nome=nome,
            imagem=imagem,
            categoria_id=categoria,
            preco=preco,
            descricao=descricao,
            quantidade=quantidade,
            codigo=codigo,
            em_estoque=em_estoque,
            data_criacao=data_criacao
        )

        return redirect('index')

    else:
        categorias = Categoria.objects.all()
        return render(request, 'pages/adicionar_produto.html', {'categorias':categorias})
    
@login_required(redirect_field_name='login')
def produto(request, id):
    detalhe = Produtos.objects.get(id=id)
    return render(request, 'pages/produto.html', {'detalhe':detalhe})

@login_required(redirect_field_name='login')
def excluir(request, id):
    produto = Produtos.objects.get(id=id)
    produto.delete()
    return redirect('index')


# GET - OBTER DADOS
# POST - ENVIAR DADOSs
# PUT - ATUALIZAR DADOS
# PATCH - ATUALIZAÇÃO PARCIAL DE DADOS    