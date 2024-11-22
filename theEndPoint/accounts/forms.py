from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator
from theEndPoint.accounts.models import Profile

UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {'username': ''}
        labels = {
            'username': 'Username:',
            'email': 'Email:',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ExampleUsername123'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'user_email@example.com'
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        password_fields = ['password1', 'password2']
        placeholders = ['Create a password...', 'Confirm your password']

        for field, placeholder in zip(password_fields, placeholders):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': placeholder
            })
            self.fields[field].help_text = None

        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password confirmation'


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        validators=[MinLengthValidator(2, message='First name is too short!')]
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        validators=[MinLengthValidator(2, message='Last name is too short!')]
    )
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = Profile
        fields = ['type_of_climber', 'age', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.instance.user

        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['email'].initial = user.email

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    def save(self, commit=True):
        profile = super().save(commit=False)

        user = profile.user

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            profile.save()
        return profile
