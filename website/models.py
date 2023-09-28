from django.db import models

class Record(models.Model):
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    renewal_date = models.DateTimeField(auto_now_add=True)
    membership = models.CharField(max_length=100)
    monthly_payment = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=800)
    sessions = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.username}"
