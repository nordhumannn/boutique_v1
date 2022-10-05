from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    class Meta:

        model = User
        fields = ('username', )
        labels = {
            'comment': '',
        }

    # username = forms.CharField(widget=forms.TextInput(), max_length=20)

    username = forms.CharField(
        label = '',
        max_length=20,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'id': 'form3Example1c',
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )

    email = forms.CharField(
        max_length=50,
        widget=forms.EmailInput(attrs={
            'type': 'email',
            'class': 'form-control',
            'name': 'email',
            'id': 'email',
            'placeholder': 'Your Email',
            'data-rule': 'email',
            'data-msg': 'Please enter a valid email'
        })
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'id': 'form3Example4c',
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'id': 'form3Exapmle4cd',
            'class': 'form-control',
            'placeholder': 'Repeat password'
        })
    )

    def clean_password2(self):
        data = self.cleaned_data

        if data['password'] == data['password2']:
            return data['password2']
        raise forms.ValidationError("Password don't match!")


class LoginUserForm(forms.Form):
    username = forms.CharField(
        label = '',
        max_length=20,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'id': 'form3Example1c',
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'id': 'form3Example4c',
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('Login or password is incorrect')

        return super().clean()
