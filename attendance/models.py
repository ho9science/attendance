from django.db import models

# Create your models here.

class Credentials(object):
    def __init__(self, access_token=None):
        self.access_token = access_token