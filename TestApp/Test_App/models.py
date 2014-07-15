from django.db import models
# Create your models here.
class Data(models.Model):
    def __str__(self):
        return self.license_title

    license_title = models.CharField(max_length=50)
    maintainer = models.CharField(max_length=50)
    private = models.BooleanField()
    maintainer_email = models.CharField(max_length=50)
    num_tags = models.IntegerField()
    
    
