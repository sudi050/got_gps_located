from django import forms
from .models import user_details

class UserForm(forms.ModelForm):
    class Meta:
        model = user_details
        fields = ['name', 'dob', 'gender', 'semester', 'branch', 'address', 'college_mail', 'phone_num']