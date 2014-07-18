import json
from django.db import models
import ast
##from jsonfield import JSONField
# Create your models here.

## List Field from:
##http://stackoverflow.com/questions/5216162/how-to-create-list-field-in-django
class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)



class Data(models.Model):
    def __str__(self):
        return self.license_title
##    def set_Resources(self):
##        resources_group_id = models.CharField(max_length=25)
##        cache_last_updated = models.DateTimeField()
##        package_id = models.CharField(max_length=50)
##        webstore_last_updated = models.DateTimeField()
##        resource_id = models.CharField(max_length=50)
##        size = models.IntegerField()
##        last_modifed = models.DateTimeField()
##        hash = models.TextField()
##        description = models.TextField()
##        format = models.CharField(max_length=30)
##        tracking_summary = models.TextField()
##        mimetype_inner = models.CharField(max_length=50)
##        mimetype = models.CharField(max_length=50)
##        cache_url = models.URLField()
##        name = models.CharField(max_length=100)
##        created = models.DateTimeField()
##        resource_url = models.URLField()
##        webstore_url = models.URLField()
##        position = models.IntegerField()
##        resource_type = models.CharField(max_length=50)

    license_title = models.CharField(max_length=50)
    maintainer = models.CharField(max_length=50)
    private = models.BooleanField()
    maintainer_email = models.CharField(max_length=50)
    num_tags = models.IntegerField()
    user_ID = models.CharField(max_length=50)
    relationships = ListField()
    license = models.CharField(max_length=50)
    metadata_modified = models.DateTimeField()
    author = models.CharField(max_length=100)
    author_email = models.EmailField()
    state = models.CharField(max_length=20)
    version = models.CharField(max_length=15)
    license_id=models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    resources = models.TextField()
    num_resources = models.IntegerField()
    tags = ListField()
    tracking_summary = models.TextField()
    groups = ListField()
    organization = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    isopen = models.BooleanField()
    notes_rendered = models.TextField()
    url = models.URLField()
    ckan_url = models.URLField()
    notes = models.TextField()
    owner_org = models.CharField(max_length=100)
    ratings_average = models.FloatField()
    extras = models.TextField()
    ratings_count = models.IntegerField()
    title = models.CharField(max_length=100)
    revision_id = models.CharField(max_length = 50)


    
    
    
    
    
