from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    indoor = models.BooleanField()
    outdoor = models.BooleanField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Seat(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='seats')
    slocation = models.CharField(max_length=100, default='no seat location')
    rating = models.CharField(max_length=100, default='no rating')
    image_url = models.CharField(max_length=200, null=True)
    reviewer = models.CharField(max_length=100, default='no reviewer')
    description = models.TextField(default='no review')
    
    def __str__(self):
        return self.slocation