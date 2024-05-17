from django.db import models

# Create your models here.
class fruit(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='media')
    sceintific_name=models.CharField(max_length=100)
    season=models.CharField(max_length=100)
    cost=models.CharField(max_length=5)

    def _str_(self):
        return self.name