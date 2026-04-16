from django.db import models


class Vazifa5(models.Model):
    STATUS_CHOICES = [
        ('yangi', 'Yangi'),
        ('jarayonda', 'Jarayonda'),
        ('tugadi', 'Tugadi'),
    ]

    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='yangi')

    def __str__(self):
        return self.title
