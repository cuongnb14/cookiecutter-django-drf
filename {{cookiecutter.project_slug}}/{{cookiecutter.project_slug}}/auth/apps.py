from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'demo.auth'
    label = "demo.auth"
    verbose_name = "Auth"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
