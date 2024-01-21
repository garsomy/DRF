from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)


class Categories(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name