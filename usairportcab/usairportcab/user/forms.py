from django import forms
from django.contrib.auth.models import User
from .models import Profile
from usapp.models import Car_fare, Sites_common_detail

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if(cd['password'] != cd['password2']):
            raise forms.ValidationError('password don\'t match.')
        return cd['password2']


class UserEditForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'phone', 'photo')

class CarFareEditForm(forms.ModelForm):
    """def __init__(self, *args, **kwargs):
        super(CarFareEditForm, self).__init__(*args, **kwargs)
        self.fields['carname'].widget.attrs['disabled'] = True
        self.fields['sitename'].widget.attrs['disabled'] = True"""

    class Meta:
        model = Car_fare
        fields = ('car_name','base_fare','min_fare','fare1','fare2','fare3','fare4','fare5','fare6','fare7','site_name')
        exclude = ('site_name',)


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = Sites_common_detail
        fields = ('logo','company_name', 'phone_no', 'email', 'website', 'address', 'list_of_holidays', 'holiday_surcharge', 'gratuity',
                  'night_charge', 'night_from_time', 'night_to_time', 'extra_seat_charge', 'stopover', 'extra_luggage', 'booking_active')
        help_texts = {
            'gratuity': 'add gratuity in % for Eg: 10 then (gratuity is 10% of estimate fare)',
            'list_of_holidays': 'eg- 10-08-2018, 01-06-2018',
            'night_from_time': 'Make sure you enter it in currect format like eg- 22:00:00',
            'night_to_time': 'Make sure you enter it in currect format like eg- 04:00:00',
            'booking_active': 'enter 1 for active and 2 for inactive service',
        }
