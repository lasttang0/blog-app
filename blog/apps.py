from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration class for the 'blog' app.

    This class defines configuration settings for the 'blog' app, such as the default auto
    field and the app's name.

    Attributes:
    - default_auto_field: The default auto field to use for models in the app.
    - name: The name of the app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
