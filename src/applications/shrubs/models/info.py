from django.db import models


class Shrubs(models.Model):
    name = models.TextField(unique=True)
    species = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    max = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
