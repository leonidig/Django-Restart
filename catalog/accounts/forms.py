from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


<<<<<<< HEAD
# Create your models here.
=======
>>>>>>> 4b18188892c36b6b01568f971ad0f2cd895fdbbf
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()

    class Meta:
        model = User
        extra_fields = ["email"]
<<<<<<< HEAD
        fields = ["username", "password1", "password2", "email"]


class ProfileUpdateForm(forms.Form):
    email = forms.EmailField(required=True, label="Email:")
    avatar = forms.ImageField(required=False, label="Avatar:")

    def clean_email(self):
        new_email = self.cleaned_data.get("email")
        if User.objects.filter(email=new_email).exists():
            raise forms.ValidationError("This email already exists")
        else:
            return new_email

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields["email"].initial = self.user.email
=======
        fields = ["username", "password1", "password2", "email"]
>>>>>>> 4b18188892c36b6b01568f971ad0f2cd895fdbbf
