from django.db import models
from django.contrib.auth.models import User


CATEGORIA = (
    ("Sala", "Sala"),
    ("Ônibus", "Ônibus"),
    ("Sem categoria", "Sem categoria")
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user}"


class Pergunta(models.Model):
    pergunta = models.TextField(default="Quem colonizou Marte?")
    perguntado_por = models.ForeignKey(Profile, models.CASCADE)
    is_active = models.BooleanField(default=True)
    resposta = models.TextField(default="Ainda sem resposta.")
    categoria = models.CharField(
        default=("Sem categoria", "Sem categoria"), choices=CATEGORIA
    )

    def __str__(self):
        return f"Pergunta: {self.pergunta}Resposta: {self.resposta}"
