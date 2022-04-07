from django.db import models

# Create your models here.


class Booking(models.Model):
    b_id = models.AutoField(primary_key=True)
    u_id = models.IntegerField()
    m_id = models.IntegerField()
    t_id = models.CharField(max_length=11)
    turflocation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    date = models.DateField()
    time = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'booking'
