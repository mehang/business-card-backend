from django.forms import ModelForm

from .models import User, Job


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'location', 'date_of_birth',
                  'profile_pic')


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'job_holder', 'employee', 'employer')