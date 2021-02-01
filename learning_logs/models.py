from django.db import models

# Create your models here.


class Topic(models.Model):
    """Theme, that user studies"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of a model"""
        return self.text


class Entry(models.Model):
    """Information that user learned about theme"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return string representation of a model"""
        return self.text[:50] + "..."
