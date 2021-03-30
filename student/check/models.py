from django.db import models
# Create your models here.


class Student(models.Model):
    name=models.TextField()
    phone=models.TextField()
    id = models.AutoField(primary_key=True,unique=True)
    school=models.TextField(default='')
    grade=models.TextField(default='')
    time=models.TextField(default='')
    date=models.TextField(default='')
    st_phone=models.TextField(default='')
    fee_day=models.TextField(default='')
    step=models.TextField(default='')

class Student_check(models.Model):
    st_id = models.ForeignKey("Student", on_delete=models.CASCADE)
    name = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)


