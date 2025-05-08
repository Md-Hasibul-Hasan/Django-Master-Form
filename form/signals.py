from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import JobCity, Job_City_Choices

@receiver(post_migrate)
def populate_job_cities(sender, **kwargs):
    """Ensure JobCity contains all predefined job cities after migration."""
    if sender.name == "form":  # Replace 'your_app_name' with your Django app name
        for city in Job_City_Choices:
            JobCity.objects.get_or_create(name=city[0])