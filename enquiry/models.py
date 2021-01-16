from django.db import models

# Create your models here.

class Enquiry(models.Model):
    Name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=20)
    email_id=models.CharField(max_length=30)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Name