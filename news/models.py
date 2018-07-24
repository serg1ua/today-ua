from django.db import models

# Create your models here.
class Article(models.Model):
    date = models.CharField(max_length=32)
    tag = models.CharField(max_length=16)
    image = models.CharField(max_length=64)
    header = models.TextField()
    six_fifty = models.TextField()
    text = models.TextField()

    def __str__(self):
        return f"{self.id} {self.date} {self.tag} {self.image} {self.header} {self.six_fifty} {self.text}"