from django.db import models

# Create your models here.



class Feedback(models.Model):
    f_id = models.IntegerField(primary_key=True)
    u_id = models.IntegerField()
    feedback = models.CharField(max_length=150)
    date = models.DateField()
    reply = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'feedback'


