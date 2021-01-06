from django.db import models

# Create your models here.

class ariza(models.Model):
    user = models.ForeignKey("auth.user",on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)

class tamirci(models.Model):
    tamirci=models.ForeignKey("auth.user",on_delete=models.CASCADE)
    service=models.CharField(max_length=25)
    explanationofservice=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)

