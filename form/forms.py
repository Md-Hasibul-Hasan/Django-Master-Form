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
        fields = [
         'name','dob','gender', 'city','pin','state','mobile','email',
         'password','confirm_password','job_city','profile_image','my_file'
        ]

        labels = {
            'name': 'Name',
            'dob': 'Date of Birth',
            'city':'City',
            'pin':'Pin Code',
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

            'pin':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Pin'}),

            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter State'}),

            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter 11 digit Mobile'}),

            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),

            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),

            'confirm_password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}),

        }








# // মডেল তৈরি না করলে এই ফর্ম বেবহার করব 


# from django import forms

# # Gender choices
# Gender_Choices = (
#     ("Male", "Male"),
#     ("Female", "Female"),
#     ("Other", "Other"),
# )

# # Job city choices
# Job_City_Choices = (
#     ("Dhaka", "Dhaka"),
#     ("Chittagong", "Chittagong"),
#     ("Khulna", "Khulna"),
#     ("Rajshahi", "Rajshahi"),
#     ("Sylhet", "Sylhet"),
#     ("Barisal", "Barisal"),
#     ("Rangpur", "Rangpur"),
#     ("Mymensingh", "Mymensingh"),
# )

# # State choices
# State_Choices = (
#     ('Dhaka', 'Dhaka'),
#     ('Chittagong', 'Chittagong'),
#     ('Khulna', 'Khulna'),
#     ('Rajshahi', 'Rajshahi'),
#     ('Sylhet', 'Sylhet'),
#     ('Barisal', 'Barisal'),
#     ('Rangpur', 'Rangpur'),
#     ('Mymensingh', 'Mymensingh'),
# )



# # Profile form
# class Profile_Form(forms.Form):
#     name = forms.CharField(
#         label='Full Name',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter full name',
#             }
#         )
#     )
#     dob = forms.DateField(
#         label='Date of Birth',
#         widget=forms.DateInput(
#             attrs={
#                 'class': 'form-control',
#                 # 'placeholder': 'Enter DOB',
#                 'id': 'datepicker', # To enable date picker in browser
#                 'type': 'date', # To enable date picker in browser
                   
#             }
#         )
#     )
#     gender = forms.ChoiceField(
#         label='Gender',
#         choices=Gender_Choices,
#         widget=forms.RadioSelect(
#             attrs={
#                 'class': '',  # Optional for Bootstrap styling
#             }
#         )
#     )
#     locality = forms.CharField(
#         label='Locality',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter locality',
#             }
#         )
#     )
#     city = forms.CharField(
#         label='City',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter city',
#             }
#         )
#     )
#     pin = forms.IntegerField(
#         label='Pin Code',
#         widget=forms.NumberInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter pin code',
#             }
#         )
#     )

#     state = forms.ChoiceField(
#         label='State',
#         choices=State_Choices,
#         widget=forms.Select(
#             attrs={
#                 'class': 'form-select', #form-select is a bootstrap class
#             }
#         )
#     )
#     mobile = forms.CharField(
#         label='Mobile Number',
#         widget=forms.NumberInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter mobile number',
#             }
#         )
#     )
#     email = forms.EmailField(
#         label='Email',
#         widget=forms.EmailInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter email',
#             }
#         )
#     )
#     password = forms.CharField(
#         label='Password',
#         help_text='At least 6 digits',
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter password',
#             }
#         )
#     )
#     c_password = forms.CharField(
#         label='Confirm Password',
#         help_text='Password should match',
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter password',
#             }
#         )
#     )
#     job_city = forms.MultipleChoiceField(
#         label='Preferred Job Cities',
#         choices=Job_City_Choices,
#         widget=forms.CheckboxSelectMultiple(
#             attrs={
#                 'class': '',  # Optional for Bootstrap styling
#             }
#         )
#     )
#     profile_image = forms.ImageField(
#         label='Profile Image',
#         required=False,
#         help_text='Upload a profile image',
#         widget=forms.ClearableFileInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         )
#     )
#     my_file = forms.FileField(
#         label='Upload File',
#         required=False,
#         help_text='Upload yout resume',
#         widget=forms.ClearableFileInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         )
#     )

#     # Custom validation for pin and pin2    
#     def clean(self):
#         cleaned_data = super().clean()
#         pass1 = cleaned_data.get('password')
#         pass2 = cleaned_data.get('c_password')
#         if pass1 != pass2:
#             raise forms.ValidationError('pass do not match')
#         if len(str(pass1)) < 6:
#             raise forms.ValidationError(' pass code at least 6 digits')
#         return cleaned_data












