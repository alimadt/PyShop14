from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail


def send_welcome_email(email):
    message = f'Спасибо за регистрацию на нашем сайте PyShop14!'
    send_mail(
        'PyShop14 Welcome', # subjext
        message,
        'pyshopadmin@gmail.com',
        [email], # кому отправляется сообщение
        fail_silently=False # если сообщение не доставится, нам придет оповещение
    )


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with such email already exists')
        return email

    def clean(self):
        data = self.cleaned_data  # это словарь
        password = data.get('password')
        password_conf = data.pop('password_confirmation')  # тк нам не нужно хранить эту переменную в data
        if password != password_conf:
            raise forms.ValidationError('Passwords do not match')
        return data

    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data)
        send_welcome_email(user.email)
        return user  # save должен возвращать только созданный объект
