from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    open_inscription = models.BooleanField(default=True)
    assistants = models.ManyToManyField(User, related_name='assistants', blank=True)

    def __str__(self):
        return '%s - %s' % (self.title, self.date)
    class Meta:
        ordering = ('-created_at',)