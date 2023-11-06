from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    link = models.URLField()


class Comment(models.Model):
    author = models.CharField(max_length=20)
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.date_published} by {self.author}'

    class Meta:
        db_table = 'comments'
        ordering = ('date_published',)

