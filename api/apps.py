from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configuration class for the 'api' app.

    This class defines configuration settings for the 'api' app, such as the default auto
    field and the app's name.

    Attributes:
    - default_auto_field: The default auto field to use for models in the app.
    - name: The name of the app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
