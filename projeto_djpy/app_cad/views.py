from django.shortcuts import render
from .models import Usuario
# Create your views here.


def home(request):
    return render(request, 'usuarios/home.html')

# Salvar os dados da tela para o banco de dados.


def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Exibir todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # retonar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)
