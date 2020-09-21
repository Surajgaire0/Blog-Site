from django.db import models
from django.urls import reverse
#from django.utils import timezone

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    publication_date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',args=[str(self.id)])

    class Meta:
        ordering=('-publication_date',)
        verbose_name_plural='posts'
