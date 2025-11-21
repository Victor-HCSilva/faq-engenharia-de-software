# 📚 MVP - Sistema de Perguntas Frequentes (FAQ)

Este projeto é um *Minimum Viable Product (MVP)* para um sistema de Perguntas Frequentes (FAQ), desenvolvido com **Django (Monolito)** e estilizado com **Bootstrap 5**. O sistema inclui autenticação de usuário, perfil editável com foto e um mecanismo de busca por texto livre em artigos FAQ.

## 🚀 Funcionalidades

*   **Login e Autenticação:** Acesso restrito a usuários cadastrados.
*   **Perfis de Usuário:** Perfil com nome completo, foto e senha/informações alteráveis.
*   **FAQ Interativo:** Listagem de perguntas frequentes na home page.
*   **Mecanismo de Busca:** Pesquisa por artigos (`icontains` em título e conteúdo) que simula a busca por temas relacionados.
*   **Artigos Detalhados:** Visualização completa de um artigo (passo a passo) com links de temas semelhantes.
*   **Painel Administrativo:** Gestão de usuários, tópicos e artigos FAQ (incluindo a marcação de 'Perguntas Frequentes' e relações 'Artigos Semelhantes').

## ⚙️ Tecnologias

*   **Backend:** Python
*   **Framework:** Django (Monolito com Class-Based Views - CBVs)
*   **Banco de Dados:** SQLite (padrão do Django)
*   **Frontend/Estilo:** HTML5, CSS3, **Bootstrap 5**, Font Awesome
*   **Gerenciamento de Pacotes:** `pip`

## 📦 Configuração e Instalação

Siga os passos abaixo para configurar e executar o projeto em sua máquina.

### 1. Pré-requisitos

Certifique-se de ter o Python 3.x instalado.

### 2. Configurar Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto.

```bash
# Crie o ambiente virtual
python3 -m venv .venv

# Ative o ambiente virtual
source .venv/bin/activate  # Para Linux/macOS
# ou
# .venv\Scripts\activate  # Para Windows (PowerShell/CMD)
```

### 3. Instalar Dependências

Com o ambiente virtual ativo, instale o Django e as bibliotecas necessárias.

```bash
(.venv) $ python -m pip install django pillow
```

> **Nota:** `Pillow` é necessário para o manuseio de uploads de imagens de perfil (`profile_image`).

### 4. Configuração Inicial do Projeto

Este projeto assume a seguinte estrutura (onde `mvp-u3` é o seu projeto principal e `faq` é o aplicativo):


Certifique-se de que seu **`settings.py`** principal está configurado corretamente:

```python
# mvp-u3/settings.py (Fragmento)

INSTALLED_APPS = [
    # ...
    'django.contrib.admin',
    # ...
    'faq', # Seu aplicativo
]

# Configuração do modelo de usuário customizado
AUTH_USER_MODEL = 'faq.CustomUser'

# Configuração de URLs de autenticação
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'

# Configuração de Arquivos de Mídia (Fotos de Perfil)
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 5. Aplicação das Migrações

Crie e aplique as migrações para inicializar o banco de dados com seus modelos (incluindo o `CustomUser`).

```bash
(.venv) $ python manage.py makemigrations faq
(.venv) $ python manage.py migrate
```

### 6. Criar Superusuário

Crie uma conta de superusuário para acessar o painel administrativo e cadastrar os artigos faq.

```bash
(.venv) $ python manage.py createsuperuser
```

### 7. Configuração de URL de Mídia (Upload de Imagens)

No seu arquivo de **URLs principal (`mvp-u3/urls.py`)**, adicione a configuração para servir arquivos de mídia durante o desenvolvimento:

```python
# mvp-u3/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('faq.urls')),
]

# Apenas para modo de desenvolvimento (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## ▶️ Como Executar

Inicie o servidor de desenvolvimento do Django:

```bash
(.venv) $ python manage.py runserver
```

Acesse o sistema em seu navegador:

*   **Página de Login:** `http://127.0.0.1:8000/login/`
*   **Painel Admin:** `http://127.0.0.1:8000/admin/`

---

## 💻 Fluxo de Utilização (MVP)

1.  **Acesse o Admin:** Entre em `/admin/` com seu superusuário.
2.  **Cadastre Conteúdo:** Adicione pelo menos um `Tópico faq` e alguns `Artigos faq`.
    *   Marque alguns artigos como **Pergunta Frequente** (`is_frequent=True`).
    *   Defina as relações de **Artigos Semelhantes** (no `faqArticle`).
3.  **Acesse a Aplicação:** Faça login com seu superusuário ou uma conta criada no admin.
4.  **Teste o Perfil:**
    *   Clique no ícone/nome do perfil na home.
    *   Acesse **Alterar Informações** para mudar o nome ou a foto.
    *   Acesse **Alterar Senha** para mudar a credencial.
5.  **Teste a Busca:** Use a barra de pesquisa na página inicial para testar a busca por conteúdo de artigos.