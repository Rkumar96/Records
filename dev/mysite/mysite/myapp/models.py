from django.db import models

# Create your models here.

class product(models.Model):
    item = models.CharField(max_length=30,null=True)
    price = models.FloatField(null=True)
    c_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.item

