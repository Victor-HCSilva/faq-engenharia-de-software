from django.forms import ModelForm
from .models import Profile, Pergunta
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
     class Meta:
         model = Profile
         fields = ["user"]

class PerguntaForm(ModelForm):
     class Meta:
         model = Pergunta
         fields = ["pergunta","resposta", "categoria"]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
