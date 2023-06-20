from django.db import models
# Create your models here


class ImageCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Foto(models.Model):
    nama = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/')
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama
