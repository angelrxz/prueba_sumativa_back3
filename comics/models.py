from django.db import models
from django.contrib.auth.models import User

class Comic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='comics/', null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    tapa_Dura = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    



    def __str__(self):
        return self.title
