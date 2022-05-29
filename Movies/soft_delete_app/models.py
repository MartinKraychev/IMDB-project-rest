from django.db import models
from django.utils import timezone

from Movies.soft_delete_app.managers import CustomManager


class SoftDeleteModel(models.Model):
    """
    ABS model that all other models inherit.
    """
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    objects = CustomManager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True
