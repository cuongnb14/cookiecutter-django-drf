from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'demo.product'
    verbose_name = "Product"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
