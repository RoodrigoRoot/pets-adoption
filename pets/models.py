from django.db import models
from django.db.models.signals import pre_save, post_save
import uuid
from django.utils.text import slugify

# Create your models here.
class Pet(models.Model):
    """
    Stoe a Pet, realted to :vaccines.Vaccine:
    """
    name = models.CharField(verbose_name="Name", max_length=50)
    breed = models.CharField(verbose_name="Breed", max_length=50)
    color = models.CharField(verbose_name="Colors", max_length=50)
    age = models.SmallIntegerField(verbose_name="Age")
    slug = models.SlugField(verbose_name="Slug")
    vaccines = models.ManyToManyField("vaccines.Vaccine", verbose_name="Vacines", through='PetsVaccine')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-pk"]
        verbose_name = "Pet"
        verbose_name_plural = "Pets"

def create_slug_pet(sender, instance, **kwargs):
    if not instance.slug:
        slug = "{}-{}".format(instance.name, str(uuid.uuid4())[:4])
        instance.slug = slug

pre_save.connect(create_slug_pet, sender=Pet)


class PetsVaccine(models.Model):
    """
    Store the put vaccine. 
    Reated with two models
    :model: Pet and Vaccine
    """
    pet = models.ForeignKey(Pet, verbose_name="Pet", on_delete=models.CASCADE)
    vaccine = models.ForeignKey("vaccines.Vaccine", verbose_name="Vaccine", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Date", auto_now=False, auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.pet.name
    

