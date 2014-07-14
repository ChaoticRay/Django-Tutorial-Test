from django.db import models

# Create your models here.
class Data(models.Model):
    def __str__(self):
        return 'User Data'

    license_title = models.CharField(max_length=100)
    maintainer = models.CharField(max_length=100)
##    private = models.BooleanField()
##    maintainer_email = models.CharField(max_length=100)
##    num_tags = models.IntegerField()
##    ID = models.CharField(max_length=100)
##    metadata_created = models.DateTimeField()
##    relationships = models.CharField(max_length=100)
##    licences = models.CharField(max_length=100)
##    metadata_modified = models.DateTimeField()
##    author = models.CharField(max_length=100)
##    author_email = models.CharField(max_length=100)
##    state = models.BooleanField()
##    version = models.CharField(max_length=100)
##    license_id = models.CharField(max_length=100)
##    Type = models.CharField(max_length=50)
##    resources = models.CharField(max_length = 50)
    
