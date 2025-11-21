from django import forms
from .models import CustomUser

# Formulário de atualização de perfil
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'profile_image', 'username']
        widgets = {
            # Oculta o campo username, mas o mantém no form para consistência
            'username': forms.TextInput(attrs={'style': 'display: none;'}), 
        }

# NOTA: O formulário de Login é tratado pela views.LoginView do Django.
# A alteração de senha é tratada pela views.PasswordChangeForm do Django.