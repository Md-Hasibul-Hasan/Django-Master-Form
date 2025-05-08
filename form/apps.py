from django.apps import AppConfig

class YourAppConfig(AppConfig):  # Replace with your actual app name
    default_auto_field = "django.db.models.BigAutoField"
    name = "form"

    def ready(self):
        import form.signals  # Ensure signals are loaded