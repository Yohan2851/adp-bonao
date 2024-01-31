from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from miembros.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Column, Row

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User  #
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Iniciar Sesión', css_class='btn bg-primary-custom'))
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-12'),
                Column('password', css_class='form-group col-md-12'),
            ))


class CustomUserCreationForm(UserCreationForm):
    codigo_de_cuenta = forms.CharField(max_length=4, required=True, help_text='Ingrese su código de cuenta.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Ingrese su nombre.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Ingrese su apellido.')
    email = forms.EmailField(max_length=254, required=True, help_text='Ingrese un correo.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'codigo_de_cuenta', 'password1', 'password2', ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # Agregar clases CSS a los campos
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-2', 'placeholder': 'Enter Username', 'id': 'username1'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-2', 'placeholder': 'Enter First name', 'id': 'first_name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control mb-2', 'placeholder': 'Enter Last name', 'id': 'last_name'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-2', 'placeholder': 'Enter Email', 'id': 'email'})
        self.fields['codigo_de_cuenta'].widget.attrs.update(
            {'class': 'form-control mb-2', 'placeholder': 'Enter Code', 'id': 'codigo_de_cuenta'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control mb-2', 'placeholder': 'Enter Password', 'id': 'password1'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control mb-2', 'placeholder': 'Enter Confirm Password', 'id': 'password2'})

        self.helper = FormHelper(self)

        self.helper.form_class = 'row g-3'

        self.helper.layout = Layout(
            Row(
                Column('username', css_class='col-md-6'),
                Column('first_name', css_class='col-md-6'),
                css_class='mb-3'
            ),
            Row(
                Column('last_name', css_class='col-md-6'),
                Column('email', css_class='col-md-6'),
                css_class='mb-3'
            ),
            Row(
                Column('password1', css_class='col-md-6'),
                Column('password2', css_class='col-md-6'),
                css_class='mb-3'
            ),
            Row(
                Column('codigo_de_cuenta', css_class='col-md-6'),
                css_class='mb-3'
            ),
            Submit('submit', 'Registrarse', css_class='btn bg-primary-custom')
        )
