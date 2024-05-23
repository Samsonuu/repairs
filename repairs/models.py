from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Repair(models.Model):
    CATEGORY_CHOICES = [
        ('廁所', '廁所'),
        ('馬桶', '馬桶'),
        ('電器', '電器'),
        ('教室', '教室'),
        ('宿舍', '宿舍'),
        ('其他', '其他'),
    ]
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES,default=' ')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.category