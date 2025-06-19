from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_area_code(value):
    if(len(str(value)) !=4):
        raise ValidationError(
            f'Area code {value} must be 4 digits long.'
        )

STATE_CHOICES = [
    ("Dhaka", "Dhaka"),
    ("Chittagong", "Chittagong"),
    ("Khulna", "Khulna"),
    ("Rajshahi", "Rajshahi"),
    ("Sylhet", "Sylhet"),
    ("Barisal", "Barisal"),
    ("Rangpur", "Rangpur"),
    ("Mymensingh", "Mymensingh"),
]

Gender_Choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

class JobCity(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Profile_Model(models.Model):
    name = models.CharField(max_length=60)
    dob = models.DateField()
    gender = models.CharField(max_length=10,
    choices=Gender_Choices)
    city = models.CharField(max_length=60,choices=STATE_CHOICES)
    area_code = models.PositiveIntegerField(help_text="Enter 4 digit area code",
    validators=[validate_area_code])
    state = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11, help_text="Enter 11 digit mobile number",
    validators=[
        RegexValidator(
            regex=r'^\d{11}$',
            message='Mobile number must be 11 digits long.',
            code='invalid_mobile'
        )
    ])
    email = models.EmailField()
    password = models.CharField(max_length=20, help_text="Enter a strong password")
    confirm_password = models.CharField(max_length=20, help_text="Re-enter the password for confirmation")
    job_city = models.ManyToManyField(
        JobCity, 
        help_text="Select job cities "
    )
    profile_image = models.ImageField(upload_to='pics', blank=True)
    my_file = models.FileField(upload_to='attachments', blank=True)

    def clean(self):
        if self.password != self.confirm_password:
            raise ValidationError({"confirm_password": "Passwords do not match"})
        if len(self.password) < 6:
            raise ValidationError({"password": "Password must be at least 6 characters"})
    


    

