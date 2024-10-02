from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = '{{cookiecutter.project_slug}}.core.auth'
    label = "{{cookiecutter.project_slug}}.core.auth"
    verbose_name = "Auth"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
