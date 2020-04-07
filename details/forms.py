from .models import Faculty
from .models import Organization
from .models import Qualification
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm
from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['image']



class QualificationForm(BSModalForm):
    # publication_date = forms.DateField(
    #     error_messages={'invalid': 'Enter a valid date in YYYY-MM-DD format.'}
    # )

    class Meta:
        model = Faculty
        fields=['qualifications']


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
