from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        if len(self.body)  > 50:
            return self.body[:50] + '...'

        else:
            return self.body

    class Meta:
        verbose_name_plural = 'articles'

    def get_absolute_url(self):
        return reverse('post_article', args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)