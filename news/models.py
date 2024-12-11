from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=25)
    information = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='brand/photo/', blank=True, null=True)

    def __str__(self):
        return self.name

class Cars(models.Model):
    name = models.CharField(max_length=50)
    created_year = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='cars/photo', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name



