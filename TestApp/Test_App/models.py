from django.db import models

# Create your models here.
class Data(models.Model):
    def __str__(self):
        return self.license_title

    license_title = models.CharField(max_length=50)
    maintainer = models.CharField(max_length=50)
    
