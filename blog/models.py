from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class Comment(models.Model):
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return (self.author.username if self.author else "무명") + "의 댓글"