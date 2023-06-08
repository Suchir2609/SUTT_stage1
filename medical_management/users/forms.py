from django import forms
from .models import User, Doctor, Appointment
from user_profile.models import Profile, Account
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        is_patient = cleaned_data.get('is_patient')
        if is_patient is True:
            cleaned_data['is_patient'] = False
        return cleaned_data

    def clean_is_staff(self):
        is_staff = self.cleaned_data.get('is_staff')
        if not is_staff:
            raise forms.ValidationError('Please select a value for is_staff.')
        return is_staff

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['is_staff'].required = True

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['age', 'gender', 'history_of_Illness']


class AppointmentUpdateForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['problems', 'doctors_wanted']


class AppointmentStatusForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['status']


class DoctorCreationForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['doctor_name', 'specialization']


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['status']

