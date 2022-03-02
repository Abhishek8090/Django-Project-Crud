from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=40)
    ename=models.TextField(max_length=100)
    role=models.TextField(max_length=100)
    email=models.TextField()

    def __str__(self):
        return str(self.eid)+" "+str(self.ename)+" "+str(self.role)+" "+str(self.email)

    class Meta:
        db_table='ttl_employees'