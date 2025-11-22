from django import forms
from .models import CustomUser

# Formulário de atualização de perfil
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'profile_image']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

# NOTA: O formulário de Login é tratado pela views.LoginView do Django.
# A alteração de senha é tratada pela views.PasswordChangeForm do Django.