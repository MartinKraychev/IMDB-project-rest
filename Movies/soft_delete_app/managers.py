from django.db import models


class CustomManager(models.Manager):
    """
    Manager that returns not deleted items
    """

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)
