from django.db import models

# Create your models here.

class Vaccine(models.Model):
    """
    Store a single vaccine
    """
    name = models.CharField(verbose_name="Vaccine", max_length=150)

    def __str__(self):
        return self.name
    