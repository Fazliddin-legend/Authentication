from django.db import models
from apps.users.models import User

class Item(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title