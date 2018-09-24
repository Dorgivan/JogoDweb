from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    username = forms.CharField(label="Nome",widget=forms.TextInput(
        attrs={'class':'form-control'}))

    email = forms.CharField(label="E-mail",widget=forms.TextInput(
        attrs={'class':'form-control'}))

    password = forms.CharField(label="Senha",widget=forms.PasswordInput(
        attrs={'class':'form-control'}))

    def save(self, commit=True):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        usuario = User.objects.create_user(
            password=password,
            username=username,
            email=email
		)
        if commit:
            usuario.save()
        return usuario

    class Meta:
        model = User
        fields = ['username','email','password']
