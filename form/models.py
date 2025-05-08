from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.apps import apps

def validate_pin_length(value):
    if len(str(value)) != 6:
        raise ValidationError("Pin code must be 6 digits")

# Gender choices
Gender_Choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

# Job city choices (Predefined)
Job_City_Choices = [
    ("Dhaka", "Dhaka"),
    ("Chittagong", "Chittagong"),
    ("Khulna", "Khulna"),
    ("Rajshahi", "Rajshahi"),
    ("Sylhet", "Sylhet"),
    ("Barisal", "Barisal"),
    ("Rangpur", "Rangpur"),
    ("Mymensingh", "Mymensingh"),
]

State_Choices=Job_City_Choices

class JobCity(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    @classmethod
    def populate_job_cities(cls):
        """Ensures JobCity model always contains predefined job cities."""
        if apps.ready:
            for city in Job_City_Choices:
                cls.objects.get_or_create(name=city[0])

class Profile_Model(models.Model):
    name = models.CharField(max_length=60)
    dob = models.DateField()
    gender = models.CharField(
        max_length=10, 
        choices=Gender_Choices
        )
    city = models.CharField(
        max_length=50,
        choices=State_Choices,
        )
    pin = models.IntegerField(
        validators=[validate_pin_length],
        help_text="Enter 6 digit pin code"
        )
    state = models.CharField(max_length=50)
    mobile = models.CharField(
        max_length=11, 
        validators=[RegexValidator(regex=r"^\d{11}$")], 
        help_text="Enter 11 digit mobile number"
    )
    email = models.EmailField()
    password = models.CharField(
        max_length=50, 
        help_text="Password must be at least 6 characters"
        )
    confirm_password = models.CharField(
        max_length=50, 
        help_text="Password and confirm password should match"
        )
    
    job_city = models.ManyToManyField(
        JobCity,
        help_text="Select job cities"
        )

    profile_image = models.ImageField(upload_to='pics', blank=True)
    my_file = models.FileField(upload_to='attachments', blank=True)

    def clean(self):
        if self.password != self.confirm_password:
            raise ValidationError({"confirm_password": "Passwords do not match"})
        if len(self.password) < 6:
            raise ValidationError({"password": "Password must be at least 6 characters"})
    








# // যদি জব সিটি আগে থেকেই না থাকে তাহলে এই কোড ব্যবহার করতে হবে। signals.py ও apps.py ফাইল লাগবে না 


# from django.db import models
# from django.core.exceptions import ValidationError
# from django.core.validators import RegexValidator

# def validate_pin_length(value):
#     if len(str(value)) != 6:
#         raise ValidationError("Pin code must be 6 digits")

# # Gender choices
# Gender_Choices = (
#     ("Male", "Male"),
#     ("Female", "Female"),
#     ("Other", "Other"),
# )

# # Job city choices (to prepopulate)
# Job_City_Choices = [
#     ("Dhaka", "Dhaka"),
#     ("Chittagong", "Chittagong"),
#     ("Khulna", "Khulna"),
#     ("Rajshahi", "Rajshahi"),
#     ("Sylhet", "Sylhet"),
#     ("Barisal", "Barisal"),
#     ("Rangpur", "Rangpur"),
#     ("Mymensingh", "Mymensingh"),
# ]

# State_Choices=Job_City_Choices


# # JobCity model to store job cities
# class JobCity(models.Model):
#     name = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name

# class Profile_Model(models.Model):
#     name = models.CharField(max_length=60)
#     dob = models.DateField()
#     gender = models.CharField(
#         max_length=10, 
#         choices=Gender_Choices
#         )
#     city = models.CharField(
#         max_length=50,
#         choices=State_Choices,
#         )
#     pin = models.IntegerField(
#         validators=[validate_pin_length],
#         help_text="Enter 6 digit pin code"
#         )
#     state = models.CharField(max_length=50)
#     mobile = models.CharField(
#         max_length=11, 
#         validators=[RegexValidator(regex=r"^\d{11}$")], 
#         help_text="Enter 11 digit mobile number"
#     )
#     email = models.EmailField()
#     password = models.CharField(
#         max_length=50, 
#         help_text="Password must be at least 6 characters"
#         )
#     confirm_password = models.CharField(
#         max_length=50, 
#         help_text="Password and confirm password should match"
#         )
    
#     job_city = models.ManyToManyField(
#         JobCity,
#         help_text="Select job cities"
#         )

#     profile_image = models.ImageField(upload_to='pics', blank=True)
#     my_file = models.FileField(upload_to='attachments', blank=True)

#     def clean(self):
#         if self.password != self.confirm_password:
#             raise ValidationError({"confirm_password": "Passwords do not match"})
#         if len(self.password) < 6:
#             raise ValidationError({"password": "Password must be at least 6 characters"})
    


