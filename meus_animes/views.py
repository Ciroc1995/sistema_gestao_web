from django.shortcuts import render, redirect, HttpResponse
from .models import Anime
from .forms import AnimeForm
from django.contrib.auth.decorators import login_required


def animes(request):
    dados = {
        'dados': Anime.objects.all()
    }
    return render(request, 'animes/animes.html', context=dados)


def detalhe(request, id_anime):
    dados = {
        'dados': Anime.objects.get(pk=id_anime)
    }
    return render(request, 'animes/detalhe.html', dados)


@login_required
def criar(request):
    if request.method == 'POST':
        anime_form = AnimeForm(request.POST)
        if anime_form.is_valid():
            anime_form.save()
        return redirect('animes')
    else:
        anime_form = {
            'anime_form': AnimeForm()
        }
        return render(request, 'animes/novo_anime.html', anime_form)


@login_required
def editar(request, id_anime):
    anime = Anime.objects.get(pk=id_anime)
    if request.method == 'POST':
        anime_form = AnimeForm(request.POST, instance=anime)
        if anime_form.is_valid():
            anime.save()
            return redirect('animes')
    else:
        anime_form = AnimeForm(instance=anime)
        anime_form = {
            'anime_form': anime_form
        }
    return render(request, 'animes/novo_anime.html', anime_form)


@login_required
def excluir(request, id_anime):
    anime = Anime.objects.get(pk=id_anime)
    if request.method == 'POST':
        anime.delete()
        return redirect('animes')
    return render(request, 'animes/confirmar_exclusao.html')
