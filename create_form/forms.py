from django import forms
from .models import Profile_Model, JobCity


# Gender choices
Gender_Choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)


class Profile_Form(forms.ModelForm):
    gender = forms.ChoiceField(
        label="Gender",
        choices=Gender_Choices,
        widget=forms.RadioSelect(),
        help_text='Your Gender'
    )

    job_city = forms.ModelMultipleChoiceField(
        queryset=JobCity.objects.all(),
        label="Prefered Job City",
        widget=forms.CheckboxSelectMultiple(),
        help_text='Select your prefered Job City'
    )


    
    class Meta:
        model = Profile_Model
        # fields = [
        #  'name','dob','gender', 'city','area_code','state','mobile','email',
        #  'password','confirm_password','job_city','profile_image','my_file'
        # ]
        fields = '__all__'

        labels = {
            'name': 'Name',
            'dob': 'Date of Birth',
            'city':'City',
            'area_code':'Area Code',
            'state':'State',
            'mobile':'Mobile Number',
            'email':'Email',
            'password':'Password',
            'confirm_password':'Confirm Password',
            'profile_image':'Profile Image',
            'my_file':'My File'
        }


        help_texts={
            'profile_image':'Upload your Profile Image',
            'my_file':'Upload your Document',
        }

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),

            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker', 'type':'date'}),

            'city':forms.Select(attrs={'class':'form-select',}),

            'area_code':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter area_code'}),

            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter State'}),

            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter 11 digit Mobile'}),

            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),

            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'},render_value=True),

            'confirm_password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'},render_value=True),
            

        }

