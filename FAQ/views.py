from django.db.models.fields.related import CASCADE
from django.shortcuts import render, redirect
from django.template import context
from .forms import (
    ProfileForm,
    PerguntaForm,
    UserForm,
)
from .models import Profile, Pergunta
from django.contrib.auth.models import User

CATEGORIAS = [
    "Sala",
    "Ônibus",
    "Sem categoria"
]

def filtrar_categorias(model: Pergunta):
    c = {
        categoria: []
        for categoria in CATEGORIAS
    }
    for k, v in c.copy().items():
        for pergunta in model.objects.filter(is_active=True):
            if pergunta.categoria == k:
                v.append(pergunta)
    return c

def login(request):
    context = {}
    return render(request, "login.html", context)

def main(request):
    profile_form_display  = ProfileForm()
    pergunta_form_display = PerguntaForm()
    user_form_display = UserForm()

    if request.method == 'POST':
        profile_form  = ProfileForm(request.POST)
        pergunta_form = PerguntaForm(request.POST)
        user_form = UserForm(request.POST)

        if profile_form.is_valid():
            print("Perfil Salvo")
            profile_form.save()
            return redirect('main')
        elif pergunta_form.is_valid():
            print("Pergunta salva")
            pergunta_form.save() # Corrigido: era is_valid()
            return redirect('main')
        elif user_form.is_valid():
            user_form.save()
        else:
            # Se nenhum formulário for válido, passe os formulários com erros
            profile_form_display = profile_form
            pergunta_form_display = pergunta_form
            print("Nenhum formulário é válido ou o formulário enviado contém erros.")
            # Para depuração, você pode imprimir os erros dos formulários:
            # print("Erros do ProfileForm:", profile_form.errors)
            # print("Erros do RespostaForm:", resposta_form.errors)
            # print("Erros do PerguntaForm:", pergunta_form.errors)

    context = {
        "profiles": Profile.objects.filter(is_active=True),
        "perguntas": Pergunta.objects.filter(is_active=True), # Corrigido o nome da chave
        "users": User.objects.filter(is_active=True),
        "form_profile": profile_form_display,
        "form_pergunta": pergunta_form_display,
        "form_user": user_form_display,
        "categorias": filtrar_categorias(Pergunta)
    }

    return render(request, "main.html", context)
