# myapp/models.py
from django.db import models

class FormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.submission_date}"
