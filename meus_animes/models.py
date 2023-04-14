from django.db import models


class Anime(models.Model):
    STATUS_CHOICES = (
        ("Não assistido", "Não assistido"),
        ("Assistido", "Assistido")
    )
    anime = models.CharField(max_length=50)
    status = models.CharField(
        max_length=50, default=False, choices=STATUS_CHOICES, blank=False, null=False)
    resenha = models.TextField(max_length=256)
