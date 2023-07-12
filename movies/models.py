from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Saloon(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']


class Ticket(models.Model):
    movie = models.ForeignKey(Movie, related_name='tickets', on_delete=models.CASCADE)
    saloon = models.ForeignKey(Saloon, related_name='tickets', on_delete=models.CASCADE)
    seat = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='tickets', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
