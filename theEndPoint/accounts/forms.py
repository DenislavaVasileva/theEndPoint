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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        the_fields = ['password1', 'password2', 'username', 'email']
        placeholders = ['Create a password...', 'Confirm your password', 'ExampleUsername123', 'user_email@example.com']
        labels = ['Password:', 'Password confirmation:', 'Username:', 'Email:']

        for field, placeholder, label in zip(the_fields, placeholders, labels):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': placeholder,
            })
            self.fields[field].label = label
            self.fields[field].help_text = None


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
        fields = ['type_of_climber', 'age', 'bio', 'profile_picture',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.instance.user

        for field in ['first_name', 'last_name', 'email']:
            self.fields[field].initial = getattr(user, field, '')

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
