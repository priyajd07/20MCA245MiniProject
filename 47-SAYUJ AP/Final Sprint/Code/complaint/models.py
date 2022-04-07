from django.db import models

# Create your models here.

class Complaint(models.Model):
    c_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField()
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    complaint = models.CharField(max_length=120)
    reply = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'complaint'
