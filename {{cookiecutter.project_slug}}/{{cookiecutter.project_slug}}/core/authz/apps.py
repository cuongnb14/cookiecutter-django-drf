from django.apps import AppConfig


class AuthzConfig(AppConfig):
    name = '{{cookiecutter.project_slug}}.core.authz'
    verbose_name = "Auth"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
