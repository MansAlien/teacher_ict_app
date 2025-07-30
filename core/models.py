import uuid

from django.db import models


class BaseModel(models.Model):
    """Base model for all models"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs) -> None:
        """Ensures a full clean before saving"""

        self.full_clean()
        return super().save(*args, **kwargs)
