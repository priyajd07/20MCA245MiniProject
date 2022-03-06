from django.db import models

# Create your models here.



class ManagerRegistration(models.Model):
    m_id = models.AutoField(primary_key=True)
    t_id = models.IntegerField()
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    turf_location = models.CharField(db_column='turf location', max_length=30)  # Field renamed to remove unsuitable characters.
    phone = models.CharField(max_length=11)
    district = models.CharField(max_length=30)
    gender = models.CharField(max_length=11)
    dob = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    repeatpassword = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'manager_registration'
