from django.apps import AppConfig


class SoftDeleteAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Movies.soft_delete_app'
