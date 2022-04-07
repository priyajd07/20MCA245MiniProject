from django.db import models

# Create your models here.

class Payment(models.Model):
    b_id = models.IntegerField()
    u_id = models.IntegerField()
    m_id = models.CharField(max_length=11)
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=20)
    amount = models.CharField(max_length=30)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'payment'
