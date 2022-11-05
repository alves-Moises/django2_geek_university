from email import message
from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm


def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        
        else:
            messages.error(request, 'erro ao enviar email')
    context = {
        'form': form
    }

    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method == 'POST'):
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)

            print(f"NOME: {prod.nome}")
            print(f"preco: {prod.preco}")
            print(f"estoque: {prod.estoque}")
            print(f"imagem: {prod.imagem}")

            messages.success(request, "PRoduto Salvo com sucesp")
            form = ProdutoModelForm()
        else:
            messages.error(request, "Erro ao salvar produto")
    else:
        form = ProdutoModelForm()

    context = {
        'form': form
    }
    return render(request, 'produto.html', context)
