from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import stu_details,job_pos
from django.forms.widgets import DateInput,CheckboxSelectMultiple
from django.http import request
from django.core.validators import MinValueValidator, MaxValueValidator




from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import stu_details  # Import your stu_details model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import stu_details  # Import your stu_details model

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import stu_details  # Import your stu_details model

class Student_SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='*required')
    last_name = forms.CharField(max_length=30, required=True, help_text='*required')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    # Fields related to stu_details model
    phone_number = forms.CharField(max_length=10, help_text='*required')
    fathers_name = forms.CharField(max_length=30, help_text='*required')
    mothers_name = forms.CharField(max_length=30, help_text='*required')
    
    # Use choices directly from the model class-level variables
    gender = forms.ChoiceField(choices=stu_details.GENDER_CHOICES, help_text='*required')
    place = forms.CharField(max_length=30, help_text='*required')
    branch = forms.ChoiceField(choices=stu_details.BRANCH_CHOICES, help_text='*required')
    
    # Fields with validation
    cgpa_Btech = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], help_text='*required')
    class_10_cgpa = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], help_text='*required')
    class_12_percentage = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='*required')
    certifications_count = forms.IntegerField(help_text='*required')
    internship = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], help_text='*required')
    languages = forms.CharField(max_length=100, help_text='*required')
    sop = forms.CharField(max_length=500, help_text='*required')
    dob = forms.DateField(help_text='*required (format: YYYY-MM-DD)')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')




class UsdForm(forms.Form):
    sop = forms.CharField(max_length=500, initial="enter ur sop",required=True)
    phone_number = forms.CharField(max_length=10,min_length=10,initial="enter ur phn num",required=True)

class dispstuForm(forms.ModelForm):
    class Meta:
        model=stu_details
        fields=('username','phone_number','fathers_name','mothers_name','gender','place','branch','cgpa_Btech','class_10_cgpa','class_12_percentage','certifications_count',\
               'internship','languages','sop','dob')


c_type = (
    ('product', 'product'),
    ('service', 'service'))


class company_SignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=30, required=True, help_text='*required')
    est_year=forms.CharField(max_length=4,required=True,help_text="*required")
    hr_name=forms.CharField(max_length=30, required=True, help_text='*required')
    hr_phn=forms.CharField(max_length=10, min_length=10,required=True, help_text='*required')
    headquaters=forms.CharField(max_length=30, required=True, help_text='*required')
    about=forms.CharField(max_length=1000, required=True, help_text='*required')
    type=forms.ChoiceField(required=True,choices=c_type)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'company_name', 'est_year','hr_name','hr_phn','headquaters','about','type','email','password1', 'password2', )


class ccdForm(forms.Form):
    hr_name = forms.CharField(max_length=30, required=True, help_text='*required')
    hr_phn = forms.CharField(max_length=10, min_length=10, required=True, help_text='*required')
    about=forms.CharField(max_length=1000, required=True, help_text='*required')


class jobposForm(forms.ModelForm):
    class Meta:
        model=job_pos
        fields=('company_name','username','job_id','designation' ,'salary'  ,'bond_years','information_technology','mech', 'civil','eee',  'ece', 'chemical' ,'cse')