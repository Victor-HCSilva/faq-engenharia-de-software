from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Modelo de Usuário Customizado (Para Perfil e Foto)
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Nome Completo")
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name="Foto de Perfil")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuário Customizado"
        verbose_name_plural = "Usuários Customizados"


# 2. Modelo de Tópico/Categoria (Para organização do FAQ)
class FAQTopic(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Título do Tópico")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tópico FAQ"
        verbose_name_plural = "Tópicos FAQ"


# 3. Modelo de Artigo FAQ (Conteúdo principal)
class FAQArticle(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título do Artigo")
    topic = models.ForeignKey(FAQTopic, on_delete=models.CASCADE, related_name='articles', verbose_name="Tópico")
    content = models.TextField(verbose_name="Conteúdo (Passo a Passo)")
    is_frequent = models.BooleanField(default=False, verbose_name="Pergunta Frequente")

    # Relação N:N para links de temas semelhantes
    similar_articles = models.ManyToManyField('self', blank=True, symmetrical=False, verbose_name="Artigos Semelhantes")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Artigo FAQ"
        verbose_name_plural = "Artigos FAQ"
        ordering = ['title']
