from django.db import models

# Create your models here.

class Categories(models.Model):
    categorie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name