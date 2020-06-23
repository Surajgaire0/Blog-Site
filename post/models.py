from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(default='default.jpg',upload_to='images/')
    description=models.TextField()
    publication_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',args=[str(self.id)])

    def summary(self):
        return self.description[:100]+'..'

    def pub_date(self):
        pass
        #return self.publication_date.strftime('')
