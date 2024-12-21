from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model


User = get_user_model()

class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(admin_forms.UserCreationForm):
    error_messages = {"duplicate_email": "This email has already been taken."}

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "email")

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError(self.error_messages["duplicate_email"])

    # def clean_username(self):
    #     username = self.cleaned_data["username"]

    #     try:
    #         User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         return username

    #     raise forms.ValidationError(self.error_messages["duplicate_username"])