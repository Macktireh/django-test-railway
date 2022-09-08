from django import forms
from django.utils.translation import gettext_lazy as _


from apps.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude = ('user',)