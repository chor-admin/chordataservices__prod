from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserProfile

class UserProfileCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ("display_name", "username", "email")

class UserProfileChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = ("display_name", "username", "email")