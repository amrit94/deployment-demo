from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class Publication(models.Model):
    title = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            articles = Article.objects.filter(publications=self.id)
            for article in articles:
                article.is_active = True
                article.save()
        elif not self.is_active:
            articles = Article.objects.filter(publications=self.id)
            for article in articles:
                article.is_active = False
                article.save()

        super().save(*args, **kwargs)


# M2M
# One article can be published -- in many publications
# One publication can have many article
class Article(models.Model):
    headline = models.CharField('Article Name', max_length=100)
    publications = models.ManyToManyField(Publication)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        if self.is_active:
            articles = Posts.objects.filter(title=self.id)
            for article in articles:
                article.is_active = True
                article.save()
        elif not self.is_active:
            articles = Posts.objects.filter(title=self.id)
            for article in articles:
                article.is_active = False
                article.save()

        super().save(*args, **kwargs)


# M2O(FK)
# One person has many posts
class Posts(models.Model):
    title = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def was_published_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title.headline

    class Meta:
        ordering = ['title']
