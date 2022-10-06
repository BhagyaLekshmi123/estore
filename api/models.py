from django.db import models
class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    publisher=models.CharField(max_length=200)
    qty=models.PositiveIntegerField(default=1)

#django orm: object relational mapping



# ormm querry for creating a object