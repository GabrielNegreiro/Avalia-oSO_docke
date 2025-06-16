from django import forms
from .models import usuario
import re
from django.contrib.auth.hashers import make_password

class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nome', 'email', 'cpf', 'senha', 'cargo']
        '''widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
            'cargo': forms.Select(attrs={'class': 'form-select'}),
        }'''
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 8:
            raise forms.ValidationError("O nome precisa ter pelo menos 8 letras.")
        return nome

    def clean_email(self):
        email = self.cleaned_data['email']
        dominios_permitidos = (
            '@gmail.com',
            '@outlook.com',
            '@hotmail.com',
            '@icloud.com',
            '@yahoo.com',
            '@google.com',
            '@microsoft.com',
            '@apple.com',
            '@amazon.com',
            '@meta.com',
            '@ibm.com',
            '@intel.com',
            '@oracle.com',
            '@spotify.com',
            '@netflix.com'
        )
        if not email.endswith((dominios_permitidos)):
            raise forms.ValidationError("Use um email que exista")
        return email
        



    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError("CPF deve conter exatamente 11 números.")
        return cpf

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        if senha:
            if len(senha) < 6:
                self.add_error('senha', "A senha deve ter pelo menos 6 caracteres.")
            if not re.search(r'[A-Z]', senha):
                self.add_error('senha', "A senha deve conter pelo menos uma letra maiúscula.")
            if not re.search(r'\d', senha):
                self.add_error('senha', "A senha deve conter pelo menos um número.")
            if not re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=/\\[\]~`]', senha):
                self.add_error('senha', "A senha deve conter pelo menos um caractere especial.")
        '''if not self.errors.get('senha'):
            cleaned_data['senha'] = make_password(senha)'''
        '''else:
        # Remover o campo se não foi passado, para não sobrescrever a senha
            cleaned_data.pop('senha', None)'''
        return cleaned_data



 
