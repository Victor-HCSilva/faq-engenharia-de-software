from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import CustomUser, FAQArticle
from .forms import CustomUserUpdateForm

# ----------------- Autenticação e Home -----------------

# 1. Login View (Wireframe: Tela de Solucione suas Dúvidas)
class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = '/'
# 2. Logout View (Padrão Django)
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# 3. Home/Search View (Wireframe: Pesquisas Frequentes)
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obter perguntas frequentes (Wireframe: Titulo A, B, C, D)
        context['frequent_questions'] = FAQArticle.objects.filter(is_frequent=True)[:5]
        context['articles'] = [] # Lista de resultados de busca
        
        search_query = self.request.GET.get('q', '')
        
        if search_query:
            # Mecânica de pesquisa icontains em Título e Conteúdo (Semanticamente relacionado)
            context['articles'] = FAQArticle.objects.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            ).distinct()
            context['search_query'] = search_query

        return context


# 4. Article Detail View (Wireframe: Titulo 4 - Conteúdo)
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = FAQArticle
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Adiciona artigos semelhantes (links no final do artigo)
        context['similar_articles'] = self.object.similar_articles.all()
        return context


# ----------------- Perfil do Usuário -----------------

# 5. Perfil Detail View (Wireframe: Perfil)
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile_detail.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user


# 6. Profile Update View (Wireframe: Alterar Informações)
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_form_kwargs(self):
        """Garante que FILES sejam incluídos no formulário para upload de imagem"""
        kwargs = super().get_form_kwargs()
        return kwargs


# 7. Password Change View (Wireframe: Alterar Informações - sub-fluxo de senha)
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('profile') # Redireciona para o perfil após a mudança
