from .models import Anime
from django.forms import ModelForm


class AnimeForm(ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'
