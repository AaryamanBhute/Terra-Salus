from django.db import models
from.storage import OverwriteStorage
from uuid import uuid4
import os
from django.utils.deconstruct import deconstructible

# Create your models here.''
@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        # set filename as random string
        filename = '{}.{}'.format("med", "png")
        # return the whole path to the file
        return os.path.join(self.path, filename)
class Image(models.Model):
    path_and_rename = PathAndRename("images/")
    img = models.FileField(upload_to=path_and_rename, storage=OverwriteStorage())
    def __str__(self):
        return('here')
class Items(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    solutions = models.TextField()