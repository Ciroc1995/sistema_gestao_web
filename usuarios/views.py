from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegistrationForm
from django.contrib import messages


def novo_usuario(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(
                request, f'O usuário {usuario} foi criado com sucesso!')
            return redirect('login')
    else:
        formulario = UserRegistrationForm()
        return render(request, 'usuarios/registrar.html', {'formulario': formulario})
