import uuid
from django.db import models

class Employee(models.Model):
    class Workplace(models.IntegerChoices):
        JOB_1 = 1, 'Junior'
        JOB_2 = 2, 'Middle'
        JOB_3 = 3, 'Senior'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workspace = models.PositiveSmallIntegerField(choices=Workplace.choices, default=Workplace.JOB_1,
                                                 help_text="Position in the company?")