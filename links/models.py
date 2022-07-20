from django.db import models
from authentication.models import User

# Create your models here.
class Links(models.Model):

    url = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.url
