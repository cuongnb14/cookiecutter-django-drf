from django.apps import AppConfig


class UserConfig(AppConfig):
    name = '{{cookiecutter.project_slug}}.user'
    verbose_name = "Users"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
