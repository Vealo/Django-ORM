import uuid
from django.db import models

class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    adress = models.CharField(max_length=50)

    def __str__(self):
        return self.phone

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Compensation(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Employee(models.Model):
    class Workplace(models.IntegerChoices):
        JOB_1 = 1, 'Junior'
        JOB_2 = 2, 'Middle'
        JOB_3 = 3, 'Senior'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workspace = models.PositiveSmallIntegerField(choices=Workplace.choices, default=Workplace.JOB_1, help_text="Position in the company?")
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, default=None)
    compensation = models.ManyToManyField(Compensation)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


